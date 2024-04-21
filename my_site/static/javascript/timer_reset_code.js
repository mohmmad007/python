function countdown(t) {
    let timer = setInterval(function() {
        let mins = Math.floor(t / 60);
        let secs = t % 60;
        document.getElementById('timer').innerText = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

        if (t < 0) {
            clearInterval(timer);
            document.getElementById('timer').innerText = 'Timer is up!';
        }

        t--;
    }, 1000);
}
let t = 7; // زمان مورد نظر را اینجا قرار دهید
countdown(t);