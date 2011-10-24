import re

def is_valid_email(email):
    if re.match("^[a-zA-Z0-9\._%\-\+]+@[a-zA-Z0-9\._%\-]+\.[a-zA-Z]{2,6}$", email) != None:    
        return True
    return False   
