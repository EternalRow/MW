import mysql.connector
import os

def dane_klienta(id):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )
        cursor = mydb.cursor()
        cursor.execute(f"SELECT first_name, last_name, balance FROM dane WHERE id={id};")
        wynik = cursor.fetchone()
        print(f"Wynik zapytania: {wynik}", flush=True)
        cursor.close()
        mydb.close()
        if wynik:
            return {"name": wynik[0], "surname": wynik[1], "balance": wynik[2]}
        return False
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False

