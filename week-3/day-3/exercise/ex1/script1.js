let animate = document.getElementById('animate')


let pixels
let interval;
function myMove() {
    pixels = 0
    interval = setInterval(myAnime,5)
}
function myAnime() {
    animate.style.left = pixels+'px'
    animate.style.top = pixels+'px'
    if (pixels === 350 ){
        clearInterval(interval)
    }
    else{
        pixels++
    }
}