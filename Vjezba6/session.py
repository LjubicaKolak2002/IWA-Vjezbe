#!python.exe
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



def add_to_session2(user):
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    for key, value in user.items():
        data = value

    db.replace_session(str(session_id), data)


def get_session():
    session_id = get_or_create_session_id()
    _, data = db.get_session(session_id)
    return data

def destroy_session():
    cookies_object = cookies.SimpleCookie()
    session_id = get_or_create_session_id()
    cookies_object["session_id"] = ""
    cookies_object["session_id"]["expires"] = 'Thu, 01 Jan 2021 00:00:00 GMT'
    print (cookies_object.output()) 
    
    query = "DELETE FROM sessions WHERE session_id = (%s)"
    values = (session_id,)
    mydb = db.get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()

    








