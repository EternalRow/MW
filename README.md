# MW -  Wykrywanie podejrzanych logowań, aplikacja wielokontenerowa


## Dokumentacja API; oczekiwane odpowiedzi

### Healthcheck:
curl.exe -X GET http://localhost:8080/api/health
> {"status":"ok"}

### Dane konkretnego klienta
Dla przykładowej sesji z ciasteczkiem o ID = 10:

curl -X 'GET' 'http://localhost:8080/api/klient' -H 'accept: */*' -H 'Cookie: session_id=10'
> np. {"imie":"Jan ","nazwisko":"Kowalski","balans":0.00}

### Dane dot. wszystkich logowań

curl.exe -X 'GET' 'http://localhost:8080/api/admin' -H 'accept: */*'

### Usunięcie logowania z tabeli
Dla przykładowego logowania o ID=1

curl.exe -X 'DELETE' 'http://localhost:8080/api/admin/1' -H 'accept: */*'
> {"deleted":true}

lub w przypadku nieistniejącego ID:
> {"deleted":false}

### Zmiana typu zagrożenia dla zapisanego logowania
Dla przykładowego logowania o ID=1

curl.exe -X 'POST' 'http://localhost:8080/api/admin/1' -H 'accept: */*'
> {"modified":true}

lub w przypadku nieistniejącego ID:
> {"modified":false}

### Usunięcie sesji
Dla przykładowej sesji z ciasteczkiem o ID = 10:

curl.exe -X 'DELETE' 'http://localhost:8080/api/sesja' -H 'accept: */*' -H 'Cookie: session_id=10'

> True

lub False w przypadku np. błędnego ID sesji

---
## Legenda wartości type

W tabeli logi kolumna type oznacza:
- 0 - nie wykryto podejrzanego logowania
- 1 - 3 nieudane proby logowania na to samo konto w ciagu 10 minut
- 2 - 3 nieudane proby z jednego adresu IP w ciagu 10 minut
- 3 - min 3 roznych adresy ip probują zbruteforceować jedno konto w ciągu 10 minut
- 4 - próba wstrzykiwania SQL
- 5 - min 3 próby logowania z tym samym błędnym hasłem w ciągu 10 minut
- 6 - udane logowanie w ciągu 10 minut z dwóch różnych adresów IP
- 7 - logowanie manualnie oznaczone jako podejrzane przez administratora
---

09.10.2026 - google AI użyte do poznania przykładu implementacji narzędzia fastapi (jak uzyc RedirectResponse i polaczyc to z formularzem) i konstrukcji Dockerfile

Wyrażenie Regex wykrywające SQL Injection w całości zaczerpnięte ze strony regex101.com