import hashlib
import os
import db

def hash_password(password):
    password_bin = password.encode('utf-8')
    salt = os.urandom(32)
    hash = hashlib.pbkdf2_hmac(
        'sha256', password_bin, salt, 100000
    )
    return salt + hash
    

def verify_password(password_text, password_hash):
    salt = password_hash[:32]
    key = password_hash[32:]
    new_hash = hashlib.pbkdf2_hmac('sha256', password_text.encode('utf-8'), salt, 100000)
    return (key == new_hash)



def change_password(username, password, new_password):
    user = db.get_user(username)
    if (user and verify_password(password, user[3])):
        if db.update_password(user[0], username, user[2], new_password): 
            return True
    else:
        return False
    