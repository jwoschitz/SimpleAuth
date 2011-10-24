import sys
import MySQLdb
import getpass

sys.path.append('../src')
import auth

config_file = 'config.cfg'

auth_handler = auth.AuthHandler(config_file)

def output(msg):
    print ">> " + msg
    
def unknown_cmd():
    output("Command unknown. Please check input.")

def truncate_tables():
    config = auth.Config(config_file)
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
    output("Tables truncated.")
    
def create_user():
    email = raw_input("Enter email address:")
    password = getpass.getpass()
    try:
        auth_handler.create_user(email, password)
        output("User '{0}' created. You will get your activation email soon".format(email))
    except auth.EmailIsInvalidError, e:
        output(e.msg)
    except auth.PasswordToShortError, e:
        output(e.msg)
    except auth.EmailAlreadyInUseError, e:
        output(e.msg)
    except auth.EmailTooLongError, e:
        output(e.msg)
        
def login():
    email = raw_input("Enter email address:")
    password = getpass.getpass()
    user = auth_handler.login(email,password)
    if user.is_logged_in:
        output("Login successful.")
        output("THE SECRET MESSAGE")
    else:
        result = {
            auth.LoginResult.USER_OR_PASSWORD_WRONG : "Wrong email or password.",
            auth.LoginResult.USER_IS_NOT_ACTIVATED : "Email is not activated.",
            auth.LoginResult.USER_IS_LOCKED_OUT : "Account has been locked."              
        }
        output(result.get(user.login_result))
        
def activate_user():
    identifier = raw_input("Please enter identifier:")
    token = raw_input("Please enter activation token:")
    activated = auth_handler.activate_user(identifier, token)
    if activated:
        output("Your account has been activated.")
    else:
        print "Invalid activation token / link."
        input = raw_input("Do you want so send a new activation mail?: (y to resend mail) ")
        if input == 'y':
            resend_mail(email)

def resend_mail(email = None):
    if not email:
        email = raw_input("Enter email address:")
    auth_handler.resend_activation_email(email)
    output("A new activation email has been sent to '{0}'".format(email))
        
while 1:
    print "Available commands:"
    print "1 - create a new user"
    print "2 - activate a created user by email activation token"
    print "3 - login and show secret message"
    print "4 - resend activation mail"
    print "r - resets the database (truncates tables)"
    print "q or exit - exit the application"
    input = raw_input("Your choice: ")
    if input == "exit" or input == "q":
        output("Bye bye")
        break
    result = {
                '1' : create_user,
                '2' : activate_user,
                '3' : login,
                '4' : resend_mail,
                'r' : truncate_tables
            }
    result.get(input, unknown_cmd)()


        