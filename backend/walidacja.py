import mysql.connector
import os


def walidacja(user, passwd):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )

        cursor = mydb.cursor()
        query = "SELECT * FROM dane WHERE email=%s AND password=%s;"
        cursor.execute(query, (user, passwd))
        wynik = cursor.fetchone()
        # print(f"Wynik zapytania: {wynik}", flush=True)
        cursor.close()
        mydb.close()
        if wynik:
            if wynik[7] == 1:  # sprawdza czy admin==true
                return 2
            return 1
        return 0
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return 0
    