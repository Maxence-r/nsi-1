function gethp() {
    fetch('https://maxencelearn-miniature-train-rq79j5qq77xfp49g-3000.preview.app.github.dev/hp')
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
    fetch('https://maxencelearn-miniature-train-rq79j5qq77xfp49g-3000.preview.app.github.dev/jj')
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
    fetch(`https://maxencelearn-miniature-train-rq79j5qq77xfp49g-3000.preview.app.github.dev/auth/${input}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) return document.getElementById('input').style.border = '1px solid red'
            document.getElementById('input').style.border = '1px solid #C8C8C8'
            console.log(data);   
        })
}



