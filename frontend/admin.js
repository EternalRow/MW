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
        blok=document.getElementById('tabela');
        let table = '<table id="logi"><tr><th>ID</th><th>Podany email</th><th>Hasło</th><th>Zalogowano?</th><th>Czas</th><th>IP</th><th>Typ zagrożenia</th></tr>';
        let zalogowano = ""
        for (let i = 0; i < data.length; i++) {
            
            if (data[i].log_in==0){zalogowano = "NIE";}else{zalogowano = "TAK";}

            if (Number(data[i].type) > 0){
                table += `<tr style="color: red;"><td>${data[i].id}</td><td>${data[i].email_input}</td><td>${data[i].pass_input}</td><td>${zalogowano}</td><td>${data[i].log_time}</td><td>${data[i].ip}</td><td>${data[i].type}</td></tr>`;
            }else{
                table += `<tr><td>${data[i].id}</td><td>${data[i].email_input}</td><td>${data[i].pass_input}</td><td>${zalogowano}</td><td>${data[i].log_time}</td><td>${data[i].ip}</td><td>${data[i].type}</td></tr>`;
            }
        }
        table += '</table>';
        blok.innerHTML += table;

        lista = document.getElementById("lista_wyboru_id");
        let opcje="";
        for (let i=0;i<data.length;i++){
            opcje += `<option value=${data[i].id}>${data[i].id}</option>`;
        }
        lista.innerHTML += opcje;
    });

document.getElementById('button_usun').addEventListener('click', async function() {
    let idWpisu = document.getElementById('input_id_wpisu').value.trim();
    if (!idWpisu){
        alert("Musisz podać ID wpisu do usunięcia.")
        return;
    }
    
    fetch(`${API_URL}admin/${encodeURIComponent(idWpisu)}`, {
        method: 'DELETE',
        credentials: 'include'
    })

    window.location.reload()

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
