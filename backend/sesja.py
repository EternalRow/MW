import mysql.connector
import random
import os

def gen_sesje(user):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )

        wynik=True
        cursor = mydb.cursor()
        while wynik:
            session_num=random.uniform(1,1000)
            query = "SELECT * FROM sesje WHERE id=%s;"
            cursor.execute(query, (session_num,))
            wynik = cursor.fetchone()

        print(f"Wynik zapytania: {wynik}", flush=True)

        query = "SELECT id FROM dane WHERE email=%s;"
        cursor.execute(query, (user,))
        wynik = cursor.fetchone()
        print(f"Wynik zapytania: {wynik[0]}", flush=True)
        query = "INSERT INTO sesje VALUES (%s, %s);"
        cursor.execute(query, (session_num, wynik[0]))
        cursor.close()
        mydb.commit()
        mydb.close()
        return session_num
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False

def pobierz_uzytkownika(session_id):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )
        cursor = mydb.cursor()
        query = "SELECT user_id FROM sesje WHERE id LIKE %s;"
        cursor.execute(query, (session_id,))
        wynik = cursor.fetchone()
        print(f"Wynik zapytania: {wynik}", flush=True)
        cursor.close()
        mydb.close()
        if wynik:
            return wynik[0]
        return False
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False

def usun_sesje(session_id):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )
        cursor = mydb.cursor()
        query = "DELETE FROM sesje WHERE id=%s;"
        cursor.execute(query, (session_id,))
        cursor.close()
        mydb.commit()
        mydb.close()
        return True
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False