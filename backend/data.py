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
            return {"imie": wynik[0], "nazwisko": wynik[1], "balans": wynik[2]}
        return {"error": "Brak danych"}
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return {"error": str(e)}

def dane_admina():
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM dane;")
        wynik = cursor.fetchall()
        print(f"Wynik zapytania: {wynik}", flush=True)
        cursor.close()
        mydb.close()
        if wynik:
            return [{"id": rekord[0], "imie": rekord[1], "nazwisko": rekord[2], "email": rekord[3], "balans": rekord[4], "ip": rekord[6]} for rekord in wynik]
        return {"error": "Brak danych"}
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return {"error": str(e)}