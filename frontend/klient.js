const API_URL = "/api/";

fetch(`${API_URL}sesja`, {
    credentials: 'include'
})
    .then(response => {
        if (response.status == 404) {window.location.href = 'http://localhost:8080';}
    });

fetch(`${API_URL}klient`, {
    credentials: 'include'
})
    .then(response => response.json())
    .then(data => {
        document.querySelector('h3').textContent = `Witaj, ${data.imie} ${data.nazwisko}`;
        document.querySelector('h1').textContent = `Konto osobiste: ${data.balans} pln`;
        document.querySelector('#main').innerHTML = `<p>Tu pojawi się historia płatności użytkownika ${data.imie}...</p>`
    });

document.getElementById('logout').addEventListener('click', function() {
    fetch(`${API_URL}sesja`, {
        method: 'DELETE',
        credentials: 'include'
    })
    .then(response => {
        if (response.ok) {
            window.location.href = 'http://localhost:8080';
        } else {
            console.error('Błąd podczas wylogowywania');
        }
    });
});
