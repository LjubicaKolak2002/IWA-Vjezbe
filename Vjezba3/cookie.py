#!C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe

from http import cookies
import os
import subjects

cookies_state = {}

cookies_string = os.environ.get('HTTP_COOKIE', '')
cookie = cookies.SimpleCookie()

def create_cookie(params):
    for element in params.keys():
        if element[:4] == "stat":
            cookie[element[4:]] = params.getvalue(element)  
    print (cookie.output())                             

def get_cookies_data():
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    #print(all_cookies_object)

    if all_cookies_object:
        for key in subjects.subjects.keys():
            if all_cookies_object.get(key): 
                cookies_state[key] = all_cookies_object.get(key).value
    return cookies_state
    

    

    