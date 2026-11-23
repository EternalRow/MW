from fastapi import FastAPI, Form, Cookie
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from walidacja import walidacja
from sesja import gen_sesje, usun_sesje, pobierz_uzytkownika
from data import dane_klienta, dane_admina
from logi import zapis_log, dopisz_udane

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/login')
def pobierz_dane(username: str = Form(...), password: str = Form(...)):
    log_id = zapis_log(username, password)

    if walidacja(username, password):
        if log_id != 0:
            dopisz_udane(log_id)

        res=RedirectResponse(url='http://localhost:8080/klient.html', status_code=303)
        res.set_cookie(key="session_id", value=gen_sesje(username), httponly=True)
        return res
    return RedirectResponse(url='http://localhost:8080/index.html?error=1', status_code=303)

@app.get('/logout')
def logout():
    return RedirectResponse(url='http://localhost:8080/index.html', status_code=303)

@app.delete('/logout')
def logout_delete(session_id: str = Cookie(None)):
    return usun_sesje(session_id)

@app.get("/klient")
def klient_session(session_id: str = Cookie(None)):
    print(session_id)
    user_id = pobierz_uzytkownika(session_id)
    print(user_id)
    dane = dane_klienta(user_id)
    if "error" in dane:
        if dane["error"] == "Brak danych":
            return JSONResponse(content=dane, status_code=404) 
        else:
            return JSONResponse(content=dane, status_code=500)
    return JSONResponse(content=dane, status_code=200)

@app.get("/admin")
def admin():
    dane = dane_admina()
    if "error" in dane:
        if dane["error"] == "Brak danych":
            return JSONResponse(content=dane, status_code=404) 
        else:
            return JSONResponse(content=dane, status_code=500)
    return JSONResponse(content=dane_admina(), status_code=200)

@app.get("/health")
def health():
    return {"status": "ok"}