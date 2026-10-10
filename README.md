# MW
Wykrywanie podejrzanych logowań - aplikacja wielokontenerowa

---

Instrukcja tworzenia i uruchamiania kontenerów:

1) Tworzenie kontenera frontend
docker run -d --name frontend -p 8080:80 -v ./frontend:/usr/share/nginx/html:ro nginx:alpine

2) Tworzenie obrazu i kontenera do backendu

- wymagane w folderze ./backend są pliki Dockerfile i requirements.txt

- tworzenie obrazu:
docker build -t obraz-backend:v1 .\backend\

- tworzenie kontenera:
docker run -d --name backend -p 8000:8000 obraz-backend:v1

- strona dostępna pod localhost:8080
dane do testu:
login:123
haslo:123

09.10.2026 - google AI użyte do poznania przykładu implementacji narzędzia fastapi (jak uzyc RedirectResponse i polaczyc to z formularzem) i konstrukcji Dockerfile
