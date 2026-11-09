fetch('http://localhost:8000/klient')
    .then(response => response.json())
    .then(data => {
        document.querySelector('h3').textContent = `Witaj, ${data.name} ${data.surname}`;
        document.querySelector('h1').textContent = `Konto osobiste: ${data.balance} pln`;
    });

document.getElementById('logout').addEventListener('click', function() {
    fetch('http://localhost:8000/logout', {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            window.location.href = 'http://localhost:8000/logout';
        } else {
            console.error('Błąd podczas wylogowywania');
        }
    });
});
