Simple login module for Python 2.7.2
----------------------------------------------------
This module provides a lightweight authorization and login module

Dependencies
----------------------------------------------------
This module needs MySQLdb

Structure
----------------------------------------------------
console_demo
    contains a small demo application which uses the auth module
src
    the source code
tests
    contains the unittests

Usage
----------------------------------------------------
# create the database schema first (see schema.sql)

import auth

config_file = 'file/path/to/config.cfg'
auth_handler = auth.AuthHandler(config_file)

# an activation email will be send to the users email address, 
# this mail contains an activation token and an identifier (encoded email address)
user = auth_handler.create_user(email, password)

# we assume that we got the activation token from somewhere,
# usually the token should be included in the email (see console_demo for a concrete implementation)
user.activate(token)
user.login()

if user.is_logged_in:
    print "login successful."
else:
    result = {
        auth.LoginResult.USER_OR_PASSWORD_WRONG : "Wrong email or password.",
        auth.LoginResult.USER_IS_NOT_ACTIVATED : "Email is not activated.",
        auth.LoginResult.USER_IS_LOCKED_OUT : "Account has been locked."              
    }
    print result.get(user.login_result)
