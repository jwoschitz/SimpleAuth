import sys
import unittest
import MySQLdb
import datetime
from ConfigParser import SafeConfigParser

sys.path.append('../src')
import auth

from config import FileNotExistsError, SectionMissingError, MandatoryOptionMissingError
from database import EmailAlreadyInUseError, EmailTooLongError
import crypto

class TestConfig:    
    TRUNCATE_TABLES = True #if set to true, the database tables will be truncated on each test run
    EMAIL_ADDRESS = 'janosch.woschitz@gmail.com'
    SEND_TEST_MAIL = False #runs a test which sends a mail to the configured email address

class Files:
    CLEAN_CONFIG = 'config.cfg'
    CONFIG_WITH_MISSING_OPTION = 'missing_mandatory_option.cfg'
    CONFIG_WITH_MISSING_SECTION = 'missing_section.cfg'
    NON_EXISTING_CONFIG = 'non_existing_file'

class ConfigTest(unittest.TestCase):
    def test_create_default_config(self):
        config = auth.Config()
        self.assertEqual(config.db_host, 'localhost')
        self.assertEqual(config.smtp_port, 25)
        self.assertEqual(config.db_password, None)
        
    def test_create_config_from_file(self):
        self.failUnlessRaises(FileNotExistsError, auth.Config, Files.NON_EXISTING_CONFIG)
        self.failUnlessRaises(SectionMissingError, auth.Config, Files.CONFIG_WITH_MISSING_SECTION)
        self.failUnlessRaises(MandatoryOptionMissingError, auth.Config, Files.CONFIG_WITH_MISSING_OPTION)
        file_name = Files.CLEAN_CONFIG
        config = auth.Config(file_name)
        parser = SafeConfigParser()
        parser.read(file_name)        
        for name in parser.options(auth.Config.CONFIG_SECTION_NAME):
            value = parser.get(auth.Config.CONFIG_SECTION_NAME, name)
            c_item = filter(lambda config_item: config_item.name == name, config._config_items)[0]
            if c_item.convert_func:
                self.assertEqual(getattr(config, name), c_item.convert_func(value))
            else:
                self.assertEqual(getattr(config, name), value)            
            
class CryptoTest(unittest.TestCase):
    def test_create_salt(self):
        salt = crypto.create_salt()
        self.assertEqual(len(salt),8)

    def test_create_hash(self):
        salt = crypto.create_salt()
        self.assertEqual(crypto.create_hash("MESSAGE",salt),crypto.create_hash("MESSAGE",salt))
    
    def test_base64(self):
        text = TestConfig.EMAIL_ADDRESS
        encoded = crypto.b64_encode(text)
        self.assertEqual(text, crypto.b64_decode(encoded))
         
class DatabaseTest(unittest.TestCase):
    def setUp(self):
        truncate_tables()
        
    def test_configure(self):
        config = auth.Config(Files.CLEAN_CONFIG)
        context = auth.DbContext(config)
        self.assertEqual(context.user.exists('some.random_mail_address@provider.com'), False)
    
    def test_create_user(self):
        config = auth.Config(Files.CLEAN_CONFIG)
        context = auth.DbContext(config)   
        user = context.user
        password = 'some_password'
        user.create(TestConfig.EMAIL_ADDRESS, password)
        with self.assertRaises(EmailAlreadyInUseError):        
            user.create(TestConfig.EMAIL_ADDRESS, password)
        with self.assertRaises(EmailTooLongError):     
            user.create(str(range(0,100)), password)
        self.assertEqual(user.login(TestConfig.EMAIL_ADDRESS, password), True)

class TestMailDispatcher(auth.MailDispatcher):
    def __init__(self, mail_config):
        super(self.__class__, self).__init__(mail_config)
        self.activation_token = None    
        
    def send_mail(self, from_addr, receiver_addr, subject, template_fill_args_dictionary):
        self.activation_token = template_fill_args_dictionary["{ACTIVATION_TOKEN}"]        
        
class MailTest(unittest.TestCase):
    def test_send(self):
        config = auth.Config(Files.CLEAN_CONFIG)
        from_addr = 'testing@domain.com'
        mail_config = auth.MailConfig(config)
        dispatcher = auth.MailDispatcher(mail_config)
        template_dispatcher = auth.TemplateMailDispatcher(mail_config, config.mail_body)        
        template_dispatcher_with_html = auth.TemplateMailDispatcher(mail_config, config.mail_body, "<b>Some HTML<b><br/>Token: {ACTIVATION_TOKEN}</br><span style=\"color:red\"><b>red text</b></span>")
        if TestConfig.SEND_TEST_MAIL:            
            dispatcher.send_mail(from_addr, TestConfig.EMAIL_ADDRESS, "This is a test","This is a test message")
            dispatcher.send_mail(from_addr, TestConfig.EMAIL_ADDRESS, u"\xdcnic\xF6d\xC9 test",u"some chars: \xD0\xCE\xC9\xC6")
            template_dispatcher.send_mail(from_addr, TestConfig.EMAIL_ADDRESS, config.mail_subject, {"{ACTIVATION_TOKEN}": "1234567890"})
            template_dispatcher_with_html.send_mail(from_addr, TestConfig.EMAIL_ADDRESS, config.mail_subject, {"{ACTIVATION_TOKEN}": "1234567890"})

class ValidatorTest(unittest.TestCase):
    def test_validate_email(self):
        self.assertEqual(auth.validator.is_valid_email('test_test'), False)
        self.assertEqual(auth.validator.is_valid_email('j\xC9rgen.schmidt@test.de'), False)
        self.assertEqual(auth.validator.is_valid_email('juergen-schmidt@test.de'), True)
        self.assertEqual(auth.validator.is_valid_email('juergen+schmidt@test.de'), True)
        self.assertEqual(auth.validator.is_valid_email('juergen%schmidt@test.de'), True)
        self.assertEqual(auth.validator.is_valid_email('juergen.schmidt@test.d'), False)
        self.assertEqual(auth.validator.is_valid_email('juergen%schmidt@test.deeeeeee'), False)
            
class AuthTest(unittest.TestCase):
    def setUp(self):
        truncate_tables()
        
    def _get_initialized_test_auth_handler(self, config = None):
        config = config if config else auth.Config(Files.CLEAN_CONFIG)
        auth_handler = auth.AuthHandler(config)
        auth_handler.mail_dispatcher = TestMailDispatcher(auth.MailConfig(config))
        return auth_handler
        
    def test_create(self):        
        auth_handler = self._get_initialized_test_auth_handler()
        with self.assertRaises(auth.PasswordToShortError):
            auth_handler.create_user(TestConfig.EMAIL_ADDRESS, '123')
        with self.assertRaises(auth.EmailIsInvalidError):
            auth_handler.create_user('...@wz', '1234567890')
        password = 'abcdef'
        user = auth_handler.create_user(TestConfig.EMAIL_ADDRESS, password)
        self.assertEqual(auth_handler._db_context.user.exists(TestConfig.EMAIL_ADDRESS), True)
        self.assertEqual(user.login(password), False)
        self.assertEqual(user.login_result, auth.LoginResult.USER_IS_NOT_ACTIVATED)
        user.activate(user.mail_dispatcher.activation_token)
        self.assertEqual(user.login(password),True)
        user = auth_handler.login(TestConfig.EMAIL_ADDRESS, password)        
        self.assertEqual(user.is_logged_in, True)
        
    def test_login(self):
        auth_handler = auth.AuthHandler(Files.CLEAN_CONFIG)
        user = auth_handler.login('abc','password')
        self.assertEqual(user.is_logged_in, False)
    
    def test_resend_activation_token(self):
        auth_handler = self._get_initialized_test_auth_handler()
        password = 'abcdef'
        user = auth_handler.create_user(TestConfig.EMAIL_ADDRESS, password)
        self.assertEqual(auth_handler._db_context.user.exists(TestConfig.EMAIL_ADDRESS), True)
        self.assertEqual(user.login(password), False)
        self.assertEqual(user.login_result, auth.LoginResult.USER_IS_NOT_ACTIVATED)
        user.resend_activation_email()
        self.assertEqual(user.login(password), False)
        self.assertEqual(user.login_result, auth.LoginResult.USER_IS_NOT_ACTIVATED)
        user.activate(user.mail_dispatcher.activation_token)
        self.assertEqual(user.login(password), True)
    
    def test_failed_logins(self):
        password = 'abcdef'
        config = auth.Config(Files.CLEAN_CONFIG)
        auth_handler = self._get_initialized_test_auth_handler(config)             
        user = auth_handler.create_user(TestConfig.EMAIL_ADDRESS, password)
        user.activate(user.mail_dispatcher.activation_token)
        self.assertEqual(user.login(password),True)        
        wrong_password = 'wrong_password'
        user.login(wrong_password)
        user.login(wrong_password)
        user.login(wrong_password)
        db_context = auth.DbContext(config)
        self.assertEqual(db_context.login_attempt.get_count(user.email,config.login_attempt_expire),3)
        # inserting outdated login attempt, should not influence count
        self._insert_login_attempt_with_date(config, user.email, datetime.datetime(2011, 1, 1, 1, 0))
        self.assertEqual(db_context.login_attempt.get_count(user.email,config.login_attempt_expire),3)
        user.login(wrong_password)
        self.assertEqual(user.login_result, auth.LoginResult.USER_OR_PASSWORD_WRONG)
        user.login(wrong_password)
        user.login(wrong_password)
        self.assertEqual(user.login_result, auth.LoginResult.USER_IS_LOCKED_OUT)
        self.assertEqual(db_context.login_attempt.get_count(user.email,config.login_attempt_expire),6)
        
    def _insert_login_attempt_with_date(self, config, login, date):
        connection = MySQLdb.connect(
            config.db_host,
            config.db_user,
            config.db_password,
            config.db_catalog
        )
        cursor = connection.cursor()        
        cursor.execute(
            "INSERT INTO login_attempts (login, `timestamp`) VALUES (%s, %s)", 
            (login,date)
        )
        connection.close()
            
    def test_auth_settings(self):
        settings = auth.Settings()
        settings = auth.Settings(auth.Config(Files.CLEAN_CONFIG))
        parser = SafeConfigParser()
        parser.read(Files.CLEAN_CONFIG)
        value = int(parser.get(auth.Config.CONFIG_SECTION_NAME, 'password_min_length'))
        self.assertEqual(settings.password_min_length,value)

def truncate_tables():
    if TestConfig.TRUNCATE_TABLES:
        config = auth.Config(Files.CLEAN_CONFIG)
        connection = MySQLdb.connect(
            config.db_host, 
            config.db_user,
            config.db_password,
            config.db_catalog
        )
        cursor = connection.cursor()        
        cursor.execute("TRUNCATE TABLE users")
        cursor.execute("TRUNCATE TABLE login_attempts")
        connection.close()
            
if __name__ == '__main__':
    unittest.main()