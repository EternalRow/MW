import mysql.connector
import random

def gen_sesje(user):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password="toor",
        database="baza"
        )

        wynik=True
        cursor = mydb.cursor()
        while wynik:
            session_num=random.uniform(1,1000)
            cursor.execute(f"SELECT * FROM sesje WHERE id='{session_num}';")
            wynik = cursor.fetchone()

        print(f"Wynik zapytania: {wynik}", flush=True)

        cursor.execute(f"SELECT id FROM dane WHERE email='{user}';")
        wynik = cursor.fetchone()
        print(f"Wynik zapytania: {wynik[0]}", flush=True)
        cursor.execute(f"INSERT INTO sesje (id, user_id) VALUES ('{session_num}', {wynik[0]});")
        cursor.close()
        mydb.commit()
        mydb.close()
        return session_num
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False

def pobierz_dane_sesji(session_id):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password="toor",
        database="baza"
        )
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM baza INNER JOIN sesje ON baza.id = sesje.user_id WHERE sesje.id='{session_id}';")
        wynik = cursor.fetchone()
        print(f"Wynik zapytania: {wynik}", flush=True)
        cursor.close()
        mydb.close()
        if wynik:
            return wynik
        return False
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False