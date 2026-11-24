from fastapi import FastAPI, Form, Cookie
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from walidacja import walidacja
from sesja import gen_sesje, usun_sesje, pobierz_uzytkownika
from data import dane_klienta, dane_admina
from logi import zapis_log, dopisz_udane

app = FastAPI(root_path="/api")


@app.post('/sesja')
def pobierz_dane(username: str = Form(...), password: str = Form(...)):
    log_id = zapis_log(username, password)
    access = walidacja(username, password)
    if access > 0:
        if log_id != 0:
            dopisz_udane(log_id)
        if access == 2:
            res =RedirectResponse(url='http://localhost:8080/admin.html', status_code=303)
            res.set_cookie(key="session_id", value=gen_sesje(username), httponly=True)
            return res
        res=RedirectResponse(url='http://localhost:8080/klient.html', status_code=303)
        res.set_cookie(key="session_id", value=gen_sesje(username), httponly=True)
        return res
    return RedirectResponse(url='http://localhost:8080?error=1', status_code=303)

@app.get('/sesja')
def logout(session_id: str = Cookie(None)):
    print("brrbrrbbrb")
    if session_id == None:
        return JSONResponse(content=False, status_code=404)
    user_id=pobierz_uzytkownika(session_id)
    
    print(user_id)
    if user_id:
        return JSONResponse(content=True, status_code=200)
    else:
        return JSONResponse(content=False, status_code=404)

@app.delete('/sesja')
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