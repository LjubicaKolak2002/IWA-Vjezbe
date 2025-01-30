#!python.exe
import mysql.connector
import json
import password_hashing

db_conf = {
    "host":"localhost",
    "db_name": "subjects",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    query = "INSERT INTO sessions (data) VALUES (%s)"
    values = (json.dumps({}),)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid 

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM sessions WHERE session_id=" + str(session_id))
    myresult = cursor.fetchone()
    return myresult[0], json.loads(myresult[1])


def replace_session(session_id, data): #replace-prvo izbrisi, a onda ubaci (delete/insert)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("""
    REPLACE INTO sessions(session_id, data) 
    VALUES (%s,%s)""",
    (session_id, json.dumps(data)))
    mydb.commit()




def create_user(username, email, password):
    query = "INSERT INTO users (ime, email, password) VALUES (%s, %s, %s)"
    hash_password = password_hashing.hash_password(password)
    values = (username, email, hash_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid

def get_username(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT ime FROM users WHERE ime='" + username + "'") 
    myresult = cursor.fetchone()
    if myresult != None:  
        return False  # postoji user
    return True 


def get_email(email):
    mydb = get_DB_connection() 
    cursor = mydb.cursor()
    cursor.execute("SELECT email FROM users WHERE email='" + email + "'") 
    myresult = cursor.fetchone() 
    if myresult != None:
        return False 
    return True 


def get_user(username):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE ime='" + username + "'") 
    myresult = cursor.fetchone()
    return myresult


def login(username, password):
    user = get_user(username) 
    if (user and password_hashing.verify_password(password, user[3])): 
        return True, user[0]
    else:
        return False, None


def get_user_by_userid(user_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE id='" + str(user_id) + "'")
    myresult = cursor.fetchone()
    return myresult



def delete_session(session_id):
    query = "DELETE FROM sessions WHERE session_id = %s"
    values = (session_id,)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    

def update_password(user_id, username, email, new_password):
    query = "UPDATE users SET id=%s, ime=%s, email=%s, password=%s WHERE ime='" + username + "'"
    hash_password = password_hashing.hash_password(new_password)
    values = (user_id, username, email, hash_password)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return True


def get_subjects(year):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects WHERE godina='" + str(year) + "'")
    myresult = cursor.fetchall()
    return myresult


def get_all_of_subjects():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM subjects")
    myresult = cursor.fetchall()
    return myresult
        
def get_all_students():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE uloga='student'")
    myresult = cursor.fetchall()
    return myresult


#vjezba 6
def get_student_by_role():
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users WHERE uloga='student'")
    myresult = cursor.fetchall()
    return myresult


def get_role(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT uloga FROM users WHERE id='" + str(id) + "'")
    myresult = cursor.fetchone()
    return myresult


def get_upisni_list(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM upisni_list WHERE student_id='" + str(id) + "'")
    myresult = cursor.fetchall()
    return myresult


def get_ime_ects(id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT ime, bodovi FROM subjects WHERE id='" + str(id) + "'")
    myresult = cursor.fetchone()
    return myresult

def update_upisni_list(user_id, predmet_id, status):
    query = "UPDATE upisni_list SET student_id=%s, predmet_id=%s, status=%s WHERE (student_id='" + str(user_id) + "'AND predmet_id='" + str(predmet_id) + "')"
    values = (user_id, predmet_id, status)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return True

def insert_upisni_list(user_id, predmet_id, status):
    query = "INSERT INTO upisni_list (student_id, predmet_id, status) VALUES (%s, %s, %s)"
    values = (user_id, predmet_id, status)
    mydb = get_DB_connection()
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    return cursor.lastrowid
