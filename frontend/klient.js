fetch('http://localhost:8000/klient/1')
    .then(response => response.json())
    .then(data => {
        document.querySelector('h3').textContent = `Witaj, ${data.imie} ${data.nazwisko}`;
        document.querySelector('h1').textContent = `Konto osobiste: ${data.balans} pln`;
    });

fetch('http://localhost:8000/admin')
    .then(response => response.json())
    .then(data => {        
        blok=document.getElementById('main');
        let table = '<table id="logi"><tr><th>ID</th><th>email_input</th><th>pass_input</th><th>log_in</th><th>log_time</th><th>IP</th><th>type</th></tr>';
        for (let i = 0; i < data.length; i++) {
            table += `<tr><td>${data[i].id}</td><td>${data[i].email_input}</td><td>${data[i].pass_input}</td><td>${data[i].log_in}</td><td>${data[i].log_time}</td><td>${data[i].ip}</td><td>${data[i].type}</td></tr>`;
        }
        table += '</table>';
        blok.innerHTML += table;
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
