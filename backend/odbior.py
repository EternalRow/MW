from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from walidacja import walidacja
from sesja import gen_sesje

app = FastAPI()

@app.post('/login')
def pobierz_dane(username: str = Form(...), password: str = Form(...)):
    if walidacja(username, password):
        res=RedirectResponse(url='http://localhost:8080/klient.html', status_code=303)
        res.set_cookie(key="session_id", value=gen_sesje(username), httponly=True)
        return res
    return RedirectResponse(url='http://localhost:8080/index.html?error=1', status_code=303)

@app.post('/logout')
def logout():
    return RedirectResponse(url='http://localhost:8080/index.html', status_code=303)