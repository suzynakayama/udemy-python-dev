btn = document.querySelector("#btn");
secret = document.querySelector('.secret');

btn.addEventListener('click', () => {
    // DELETE Log
    console.log('clicked');
    secret.classList.toggle('hidden');
})