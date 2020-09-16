if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);

    /*
    if (counter % 10 == 0) {
        alert(`Count is now ${counter}`);
    }
    */
}

// Loading content, because the document.quertSelector('button').onclick = count;
// Is loaded first than <button>Count</button>
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    // setInterval(count, 1000);
});
