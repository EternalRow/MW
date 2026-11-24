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
    });

fetch(`${API_URL}admin`)
    .then(response => response.json())
    .then(data => {        
        blok=document.getElementById('main');
        let table = '<table id="logi"><tr><th>ID</th><th>email_input</th><th>pass_input</th><th>log_in</th><th>log_time</th><th>IP</th><th>type</th></tr>';
        for (let i = 0; i < data.length; i++) {
            if (Number(data[i].type) > 0){
                table += `<tr style="color: red;"><td>${data[i].id}</td><td>${data[i].email_input}</td><td>${data[i].pass_input}</td><td>${data[i].log_in}</td><td>${data[i].log_time}</td><td>${data[i].ip}</td><td>${data[i].type}</td></tr>`;
            }else{
                table += `<tr><td>${data[i].id}</td><td>${data[i].email_input}</td><td>${data[i].pass_input}</td><td>${data[i].log_in}</td><td>${data[i].log_time}</td><td>${data[i].ip}</td><td>${data[i].type}</td></tr>`;
            }
        }
        table += '</table>';
        blok.innerHTML += table;
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
