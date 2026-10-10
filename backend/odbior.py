from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from walidacja import walidacja

app = FastAPI()

@app.post('/login')
def pobierz_dane(username: str = Form(...), password: str = Form(...)):
    if walidacja(username, password):
        return RedirectResponse(url='http://localhost:8080/klient.html', status_code=303)
    return RedirectResponse(url='http://localhost:8080/index.html?error=1', status_code=303)

@app.post('/logout')
def logout():
    return RedirectResponse(url='http://localhost:8080/index.html', status_code=303)