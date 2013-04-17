# Simple Auth

This module provides a lightweight authorization and login module with almost no dependencies

## Dependencies
* This module has been written for Python 2.7, has not been tested yet with other versions.
* Currently this module needs MySQLdb, will change this in the future to support also SQLite and other database providers.

## Structure
* console_demo
    * contains a small console application which shows an example usage of the auth module
* src
    * the source code
* tests
    * contains the unittests

## Setup
1. Create the database schema manually (see [schema.sql](schema.sql)), this will change in future versions
2. Adapt config file to fit your needs, you may use [this example](console_demo/config.cfg) as a starting point
3. Import the module with `import auth`

## Example usage

```python
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
```
