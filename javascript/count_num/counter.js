let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 == 0) {
        alert(`Count is now ${counter}`);
    }
}

// Loading content, because the document.quertSelector('button').onclick = count;
// Is loaded first than <button>Count</button>
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});
