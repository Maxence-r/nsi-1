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
                let boxmain = document.getElementById(`box${i}`);
                let button = document.createElement('button');
                button.setAttribute('onclick', `getid('${element._id}')`);
                button.className = 'more';
                button.innerHTML = 'Charger Plus';
                boxmain.appendChild(button);
                document.getElementById(`owner${f}`).innerHTML = element.owner;
                Object.entries(element.first).forEach(entry => {
                    const [key, value] = entry;
                    li = document.createElement('li');
                    li.innerHTML = `${key.substring(0, 24)}<span id='score'>${value}</span>`;
                    boxdiv[0].appendChild(li);
                  });     
            });
            element = document.getElementById(`loaded`)
            element.classList.add("endloaded");
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



function getid(par) {
    element = document.getElementById(`loaded`)
    element.classList.remove("endloaded");
    element.classList.remove("chargement");
    element.classList.add("chargement");
     fetch(`${location.protocol}//${window.location.host}/auth/${par || document.getElementById('input').value}`)
        // stop if the response is not 200 OK
        .then((response) => {
            if (response.ok) {
              return response.json();
            }
            document.getElementById('input').style.border = '1px solid red';
            document.getElementById('scrollto').style.display = 'none';
          })
        .then(data => {
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
            element.classList.add("endloaded");
        }) 
}

function popup() {
    const params = new URLSearchParams(window.location.search);
    pseudo = params.get('owner');
    score = params.get('try');
    mot = params.get('word');
    id = params.get('id');
    if (pseudo && score && mot) {
        document.getElementById('popup').style.display = 'flex';
        document.getElementById('ownerpop').innerHTML = pseudo;
        document.getElementById('trypop').innerHTML = score;
        document.getElementById('wordpop').innerHTML = mot;
        document.getElementById('idpop').innerHTML = id;
    }
}

popup();

function closepop() {
    document.getElementById('popup').style.display = 'none';
}