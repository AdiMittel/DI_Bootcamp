let input = document.getElementById('input')

input.addEventListener('input', function () {
    const found = input.value.match(/[a-zA-Z]/g);
    if (found !== null) {
        input.value = found.join('');
    } else {
        input.value = input.value.slice(0, -1);
    }
});