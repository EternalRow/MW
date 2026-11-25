import mysql.connector, os, re
from datetime import datetime

def zapis_log(username, password):
    try:
        czas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )

        cursor = mydb.cursor()
        cursor.execute("SELECT MAX(id) FROM logi;")
        res = cursor.fetchone()
        max_id=0
        if res and res[0] is not None:
            max_id = int(res[0])
        log_id = max_id+1

        ip = '0.0.0.0'  # !!! zmień

        typ = testy(cursor, username, password, czas, ip)

        query = "INSERT INTO logi VALUES (%s, %s, %s, 0, %s, %s, %s);"
        cursor.execute(query, (log_id, username, password, czas, ip, typ))
        cursor.close()
        mydb.commit()
        mydb.close()
        return log_id

    except Exception as e:
        print(f"Błąd bazy: {e}")
        return 0


def dopisz_udane(log_id):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )

        cursor = mydb.cursor()

        query = "UPDATE logi SET log_in=1 WHERE id=%s;"
        
        cursor.execute(query, (log_id,))

        cursor.close()
        mydb.commit()
        mydb.close()
        return

    except Exception as e:
        print(f"Błąd bazy: {e}")
        return

def testy(cursor, username, password, czas, ip):
    '''
    Informuje o charakterze proby logowania:
    0 - nie wykryto podejrzanego logowania
    1 - 3 nieudane proby logowania na to samo konto w ciagu 10 minut
    2 - 3 nieudane proby z jednego adresu IP w ciagu 10 minut
    3 - min 3 roznych adresy ip probują zbruteforceować jedno konto w ciągu 10 minut
    4 - próba wstrzykiwania SQL
    5 - min 3 próby logowania z tym samym błędnym hasłem w ciągu 10 minut
    6 - udane logowanie w ciągu 10 minut z dwóch różnych adresów IP
    '''

    # CZY WSTRZYKIWWANIE SQL
    if sprawdz_wstrzykiwanie(username) or sprawdz_wstrzykiwanie(password):
        return 4

    # CZY >=3 NIEUDANE LOGOWANIA
    query = "SELECT COUNT(*) FROM logi WHERE email_input=%s AND log_in=0 AND log_time BETWEEN %s - INTERVAL 10 MINUTE AND %s;"
    cursor.execute(query, (username, czas, czas))
    res = cursor.fetchone()
    if res[0] >= 2:
        return 1

    # CZY JEDEN ADRES IP 
    query = "SELECT COUNT(*) FROM logi WHERE ip=%s AND log_in = 0 AND log_time BETWEEN %s - INTERVAL 10 MINUTE AND %s;"
    cursor.execute(query, (ip, czas, czas))
    res = cursor.fetchone()
    if res[0] >= 2:
            return 2

    # CZY BRUTEFORCE NA JEDNO KONTO
    query = "SELECT COUNT(DISTINCT ip) FROM logi WHERE email_input = %s and log_in=0 and log_time BETWEEN %s - INTERVAL 10 MINUTE AND %s;"
    cursor.execute(query, (username, czas, czas))
    res = cursor.fetchone()
    if res[0] >= 2:
        return 3

    # CZY TE SAMO BLEDNE HASLO MIN 3 RAZY W CIAGU 10 MINUT
    query = "SELECT COUNT(DISTINCT email_input) FROM logi WHERE pass_input=%s and log_in=0 AND log_time BETWEEN %s - INTERVAL 10 MINUTE AND %s;"
    cursor.execute(query, (password, czas, czas))
    res = cursor.fetchone()
    if res[0] >=3:
        return 5

    # LOGOWANIE NA JEDNO KONTO Z INNEGO IP
    query = "SELECT COUNT(*) FROM logi WHERE email_input = %s AND log_in = 1 AND ip != %s AND log_time BETWEEN %s - INTERVAL 30 MINUTE AND %s;"
    cursor.execute(query, (username, ip, czas, czas))
    res = cursor.fetchone()
    if res[0] >= 1:
        return 6

    return 0

def sprawdz_wstrzykiwanie(tekst):
    wzor_regex = r"(\b(select\s+.+\s+from|insert\s+.+\s+into|update\s+.+\s+set|delete\s+.+\s+from|drop\s+table|truncate\s+table|alter\s+table|exec)\b)|(\bunion\b\s+\bselect\b)|(['\";]\s*\b(or|and|union|select|drop)\b)|(\b(or|and)\b\s+['\"]?\w+['\"]?\s*[=<>!]+\s*['\"]?\w+['\"]?)|(--(\s|$)|/\*|\*/)"
    
    if not tekst:
        return False

    if re.search(wzor_regex, tekst, re.IGNORECASE):
        return True
    return False
     

def usun_wpis_log(id_wpisu: int):
    try:
        mydb = mysql.connector.connect(
        host="database",
        user="root",
        password=os.environ["MYSQL_ROOT_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
        )

        cursor = mydb.cursor()

        query = "DELETE FROM logi WHERE id=%s;"
        
        cursor.execute(query, (id_wpisu,))

        cursor.close()
        mydb.commit()
        mydb.close()
        return

    except Exception as e:
        print(f"Błąd bazy: {e}")
        return