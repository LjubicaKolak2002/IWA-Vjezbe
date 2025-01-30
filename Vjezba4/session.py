#! C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe
import db
import os
from http import cookies

def get_or_create_session_id():
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    session_id = all_cookies_object.get("session_id").value if all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print (cookies_object.output()) #upisivanje cookie-a u header
    return session_id



def add_to_session(params):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id) #vracanje do sada odabranih podataka
    for subject_id in params.keys():
        if subject_id[:4] == "stat":
            data[subject_id[4:]] = params.getvalue(subject_id)
            
    db.replace_session(session_id, data)


def get_session():
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    return data






