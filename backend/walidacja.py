import mysql.connector



def walidacja(user, passwd):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password="toor",
        database="baza"
        )

        cursor = mydb.cursor()
        cursor.execute(f"SELECT * FROM dane WHERE email='{user}' AND password='{passwd}';")
        wynik = cursor.fetchone()
        cursor.close()
        mydb.close()
        if wynik:
            return True
        return False
    except Exception as e:
        print(f"Błąd bazy: {e}")
        return False
    