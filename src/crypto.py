import hashlib
import random
import string	
import uuid
import base64

def create_salt():
    return _create_random_string(8)

def create_activation_token():
    guid = uuid.uuid1()
    return str(guid).replace("-","")

def _create_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(length))

def create_hash(text, salt):
    return hashlib.sha512( salt + text ).digest()
    
def b64_encode(text):
    return base64.b64encode(text)

def b64_decode(text):
    return base64.b64decode(text)