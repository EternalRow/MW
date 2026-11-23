# MW
Wykrywanie podejrzanych logowań - aplikacja wielokontenerowa

---
curl -X GET http://localhost:8000/health

curl -X GET http://localhost:8000/admin

curl -X GET http://localhost:8000/klient/1000


---
W tabeli logi kolumna type oznacza:
0 - nie wykryto podejrzanego logowania
1 - 3 nieudane proby logowania na to samo konto w ciagu 10 minut
2 - 3 nieudane proby z jednego adresu IP w ciagu 10 minut
3 - min 3 roznych adresy ip probują zbruteforceować jedno konto w ciągu 10 minut
4 - próba wstrzykiwania SQL
5 - min 3 próby logowania z tym samym błędnym hasłem w ciągu 10 minut
6 - udane logowanie w ciągu 10 minut z dwóch różnych adresów IP

---

09.10.2026 - google AI użyte do poznania przykładu implementacji narzędzia fastapi (jak uzyc RedirectResponse i polaczyc to z formularzem) i konstrukcji Dockerfile

Regex wykrywający SQL Injection w całości zaczerpnięty ze strony regex101.com