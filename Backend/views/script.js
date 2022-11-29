function gethp() {
    fetch('http://localhost:3000/hp')
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
                    li.innerHTML = `${key}<span id='score'>${value}</span>`;
                    boxdiv[0].appendChild(li);
                  });
            });
        })
}

gethp();


function getjj() {
    fetch('http://localhost:3000/jj')
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



