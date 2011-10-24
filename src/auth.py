from config import Config
from database import DbContext, EmailAlreadyInUseError, EmailTooLongError
from exception import Error
from mail import TemplateMailDispatcher, MailDispatcher, MailConfig
import validator
import crypto

class LoginResult:
    NONE = 0
    SUCCESS = 1
    USER_OR_PASSWORD_WRONG = 2
    USER_IS_NOT_ACTIVATED = 3
    USER_IS_LOCKED_OUT = 4

class PasswordToShortError(Error):
    def __init__(self, min_chars):
        super(self.__class__, self).__init__("The password must be at least {0} characters long.".format(min_chars))

class EmailIsInvalidError(Error):
    def __init__(self, email):
        super(self.__class__, self).__init__("The email address '{0}' contains invalid characters.".format(email))
        
class Settings(object):
    def __init__(self, config = None):
        self._set_attr_from_config("password_min_length", config)
        self._set_attr_from_config("login_attempt_expire", config)
        self._set_attr_from_config("login_max_attempts", config)
        self._set_attr_from_config("mail_activation_expire", config)
        self._set_attr_from_config("mail_from", config)
        self._set_attr_from_config("mail_subject", config)
        self._set_attr_from_config("mail_body", config)
        self._set_attr_from_config("mail_body_html", config)
        
    def _set_attr_from_config(self, attr_name, config):
        value = getattr(config,attr_name) if config else None
        setattr(self, attr_name, value)

class AuthHandler(object):   
    def __init__(self, config_or_file_path):
        config = self._get_config(config_or_file_path)
        self._configure(config)
        
    def _get_config(self, config_or_file_path):
        if isinstance(config_or_file_path, Config):
            return config_or_file_path
        else:
            return Config(config_or_file_path)                      
    
    def _configure(self, config):
        self._db_context = DbContext(config)
        self.settings = Settings(config)
        self.mail_dispatcher = TemplateMailDispatcher(MailConfig(config), self.settings.mail_body, self.settings.mail_body_html)

    def create_user(self, email, password):
        user = self.get_user(email)
        user.create(password)
        return user
        
    def activate_user(self, encoded_email, activation_token):        
        email = crypto.b64_decode(encoded_email)
        user = self.get_user(email)
        activated = user.activate(activation_token)
        return activated
    
    def resend_activation_email(self, email):
        user = self.get_user(email)
        user.resend_activation_email()
        return user
    
    def get_user(self, email):
        return User(email, self._db_context, self.settings, self.mail_dispatcher)

    def login(self, email, password):
        user = self.get_user(email)
        user.login(password)
        return user
        
class User(object):    
    def __init__(self, email, db_context, settings, mail_dispatcher):
        self._db_context = db_context
        self.settings = settings
        self.mail_dispatcher = mail_dispatcher
        self.email = email
        self.is_logged_in = False
        self.login_result = LoginResult.NONE

    def get_is_activated(self):
        return self._db_context.user.is_activated(self.email)
        
    is_activated = property(get_is_activated)
    
    def create(self, password):
        if not validator.is_valid_email(self.email):
            raise EmailIsInvalidError(self.email)   
        if len(password) < int(self.settings.password_min_length):
            raise PasswordToShortError(self.settings.password_min_length)     
        activation_token = self._db_context.user.create(self.email, password)
        self._send_activation_token(activation_token)
        
    def resend_activation_email(self):
        activation_token = self._db_context.user.renew_activation_token(self.email)
        self._send_activation_token(activation_token)
    
    def _send_activation_token(self, activation_token):
        if activation_token:
            encoded_email = crypto.b64_encode(self.email)
            self.mail_dispatcher.send_mail(
                self.settings.mail_from, 
                self.email, 
                self.settings.mail_subject, 
                {"{ACTIVATION_TOKEN}": activation_token, "{EMAIL_IDENTIFIER}": encoded_email})
            
    def activate(self, activation_token):
        activated = self._db_context.user.activate(self.email, activation_token, self.settings.mail_activation_expire)
        return activated
    
    def login(self, password):
        if self._db_context.login_attempt.is_locked_out(self.email, self.settings.login_attempt_expire, self.settings.login_max_attempts):
            self.login_result = LoginResult.USER_IS_LOCKED_OUT
            self._db_context.login_attempt.log_failed_attempt(self.email)
            return False
            
        if not self.is_activated:
            self.login_result = LoginResult.USER_IS_NOT_ACTIVATED
            return False
            
        self.is_logged_in = self._db_context.user.login(self.email, password)            
        if self.is_logged_in:
            self.login_result = LoginResult.SUCCESS
            return True
            
        self.login_result = LoginResult.USER_OR_PASSWORD_WRONG
        self._db_context.login_attempt.log_failed_attempt(self.email)
        return False            