import MySQLdb
import crypto
from exception import Error

class EmailAlreadyInUseError(Error):
    def __init__(self, email):
        super(self.__class__, self).__init__("Email '{0}' is already registered.".format(email))

class EmailTooLongError(Error):
    def __init__(self, email, max_chars):
        super(self.__class__, self).__init__("Your email '{0}' is too long. Email address must be short than {1} characters.".format(email,max_chars))        
        
class DbConnectionConfig(object):
    def __init__(self, db_host, db_user, db_password, db_catalog):
        self.db_host = db_host
        self.db_user = db_user
        self.db_password = db_password
        self.db_catalog = db_catalog
        
class DbConnection(object): 
    is_connected = None
    db_connection = None
    
    def __init__(self, db_connection_config):
        self.db_host = db_connection_config.db_host
        self.db_user = db_connection_config.db_user
        self.db_password = db_connection_config.db_password
        self.db_catalog = db_connection_config.db_catalog
    
    def connect(self):
        if not self.is_connected():
            self.db_connection = MySQLdb.connect(
                self.db_host, 
                self.db_user,
                self.db_password,
                self.db_catalog
            )
    
    def execute_query_row(self, sql, params = None, keep_connection_open = False):
        return self.__query(sql, params,'row')
     
    def execute_query_all(self, sql, params = None, keep_connection_open = False):
        return self.__query(sql, params,'all')
    
    def execute_scalar(self, sql, params = None, keep_connection_open = False):
        row = self.__query(sql, params,'row')
        if row:
            return row[0]
        return None        
    
    def execute_non_query(self, sql, params = None, keep_connection_open = False):
        self.__query(sql, params)
    
    def __query(self, sql, params = None, returnValue = None, keep_connection_open = False):
        try:
            self.connect()
            cursor = self.db_connection.cursor()
            cursor.execute(sql, params)        
            result = {
                'row' : cursor.fetchone(),
                'all' : cursor.fetchall()
            }
            return result.get(returnValue)
        finally:
            if not keep_connection_open:
                self.close()
        
    def close(self):
        if self.is_connected():
            self.db_connection.close()
            self.db_connection = None
        
    def is_connected(self):
        if self.db_connection:
            return True
        return False

class DbContext(object):    
    def __init__(self, config):
        connection_config = DbConnectionConfig(
            config.db_host,
            config.db_user,
            config.db_password,
            config.db_catalog
        )
        self.db_connection = DbConnection(connection_config)
        self.user = User(self.db_connection)
        self.login_attempt = LoginAttempt(self.db_connection)     
        
class LoginAttempt(object):   
    def __init__(self, db_connection):
        self._db_connection = db_connection
        
    def log_failed_attempt(self, email):
        self._db_connection.execute_non_query(
            "INSERT INTO login_attempts (login) VALUES (%s)", email
        )
     
    def is_locked_out(self, email, login_attempt_expire, login_max_attempts):
        if self.get_count(email, login_attempt_expire) >= login_max_attempts:
            return True
        return False
            
    def get_count(self, email, login_attempt_expire):
        result = self._db_connection.execute_scalar(
            "SELECT COUNT(id) FROM login_attempts WHERE login = %s AND timestamp > DATE_SUB(NOW(), INTERVAL %s SECOND)",
            (email, login_attempt_expire)
        )
        return int(result)
        
class User(object):
    def __init__(self, db_connection):
        self._db_connection = db_connection

    def is_activated(self, email, keep_connection_open = False):
        return self._db_connection.execute_scalar("SELECT is_activated FROM users WHERE email = %s LIMIT 1", email, keep_connection_open)   
    
    def exists(self, email, keep_connection_open = False):
        value = self._db_connection.execute_scalar("SELECT id FROM users WHERE email = %s LIMIT 1", email, keep_connection_open)
        return value is not None
        
    def create(self, email, password):
        if self.exists(email):
            raise EmailAlreadyInUseError(email)
        if len(email) > 100:
            raise EmailTooLongError(email, 100)
        activation_token = crypto.create_activation_token()
        salt = crypto.create_salt()
        hashed_password = crypto.create_hash(password,salt)
        self._db_connection.execute_non_query(
            ("INSERT INTO users (email, password, salt, activation_token, activation_token_requested, created)"
            "VALUES (%s, %s, %s, %s, NOW(), NOW())"),
            (email, hashed_password, salt, activation_token)
        )
        return activation_token
    
    def renew_activation_token(self, email):
        if not self.exists(email):
            return
        if self.is_activated(email):
            return
        activation_token = crypto.create_activation_token()
        self._db_connection.execute_non_query(
            ("UPDATE users SET activation_token = %s, activation_token_requested = NOW()"
            "WHERE email = %s"), (activation_token, email)
        )
        return activation_token
    
    def activate(self, email, activation_token, email_activation_expire):
        token = self._db_connection.execute_scalar(
            "SELECT activation_token FROM users WHERE email = %s AND activation_token_requested > DATE_SUB(NOW(), INTERVAL %s SECOND)", 
            (email, email_activation_expire)
        )
        if not token == activation_token:
            return False
        self._db_connection.execute_non_query(
            "UPDATE users SET is_activated = 1 WHERE email = %s", email
        )
        return True
    
    def login(self, email, password):
        try:
            salt = self._get_salt_from_db(email, True)
            hashed_password = crypto.create_hash(password, salt)
            result = self._db_connection.execute_scalar(
                "SELECT id FROM users WHERE email = %s AND password = %s LIMIT 1",
                (email, hashed_password)
            )            
        finally:
            self._db_connection.close()
        return result is not None       
        
    def _get_salt_from_db(self, email, keep_connection_open = False):
        return self._db_connection.execute_scalar("SELECT salt FROM users WHERE email = %s LIMIT 1", email, keep_connection_open)    