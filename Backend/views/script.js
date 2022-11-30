function gethp() {
    fetch(`${location.protocol}//${window.location.host}/hp`)
        .then(response => response.json())
        .then(data => {
            i = 0;
            f= 0;
            data.forEach(element => {
                i = i + 1;
                f = f + 1;
                let boxdiv = document.querySelectorAll(`.ullist${i}`);
                document.getElementById(`owner${f}`).innerHTML = element.owner;
                Object.entries(element.first).forEach(entry => {
                    const [key, value] = entry;
                    li = document.createElement('li');
                    li.innerHTML = `${key.substring(0, 24)}<span id='score'>${value}</span>`;
                    boxdiv[0].appendChild(li);
                  });
            });
        })
}

gethp();


function getjj() {
    fetch(`${location.protocol}//${window.location.host}/jj`)
        .then(response => response.json())
        .then(data => {
            i = 0;
            data.forEach(element => {
                console.log(element);
                i = i + 1;
                document.getElementById(`ownerjj${i}`).innerHTML = element.owner.substring(0, 15);
                document.getElementById(`word${i}`).innerHTML = element.word;
                document.getElementById(`guess${i}`).innerHTML = element.try.toString();
            });
        })
}

getjj();



function getid() {
    input = document.getElementById('input').value;
     fetch(`${location.protocol}//${window.location.host}/auth/${input}`)
        .then(response => response.json())
        .then(data => {
            if (!data || data.error) return document.getElementById('input').style.border = '1px solid red'
            document.getElementById('moyenne').innerHTML = data.moyenne;
            document.getElementById('statowner').innerHTML = data.owner;
            document.getElementById('input').style.border = '1px solid #C8C8C8'
            f = 1
            licheck = document.querySelectorAll('.li');
            if (licheck) {
                licheck.forEach(element => {
                    element.remove();
                });
            }
            for (const [key, value] of Object.entries(data.content)) {
                let li = document.createElement('li');
                li.className = 'li';
                li.innerHTML = `<li class="scorelist"><span id="scorepseudo">${key}<span id="scorerank">#${f}</span></span><span id="scorestat">${value}</span></li>`;
                document.getElementById('scorelist').appendChild(li);
                f = f + 1;
              }
              document.getElementById('scrollto').style.display = 'flex';
              document.getElementById('scrollto').scrollIntoView();
        })
}



