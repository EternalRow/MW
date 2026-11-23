fetch(`http://localhost:8000/klient`, {
    credentials: 'include'
})
    .then(response => response.json())
    .then(data => {
        document.querySelector('h3').textContent = `Witaj, ${data.imie} ${data.nazwisko}`;
        document.querySelector('h1').textContent = `Konto osobiste: ${data.balans} pln`;
    });

fetch('http://localhost:8000/klient',{
        credentials: 'include'
})
    
    .then(response => response.json())
    .then(data => {        
        blok=document.getElementById('main');
        let text = `<p>Tu pojawi się historia płatności użytkownika ${data.imie}...</p>`;
        blok.innerHTML += text;
    });

document.getElementById('logout').addEventListener('click', function() {
    fetch('http://localhost:8000/sesja', {
        method: 'DELETE',
        credentials: 'include'
    })
    .then(response => {
        if (response.ok) {
            window.location.href = 'http://localhost:8000/sesja';
        } else {
            console.error('Błąd podczas wylogowywania');
        }
    });
});
