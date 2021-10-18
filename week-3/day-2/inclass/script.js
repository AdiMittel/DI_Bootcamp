// Exercise

// 1. Create two buttons - id of "red", id of "blue"
// 2. When we click on the red button -> Change the backgroundcolor of
//  the page to red
// 3. the same for blue

function redBtn() {
    document.querySelector('body').style.backgroundColor = 'red'
}
function blueBtn() {
    document.querySelector('body').style.backgroundColor = 'blue'
}

let redButton = document.querySelector('#red')
let blueButton = document.querySelector('#blue')

redButton.addEventListener('click',redBtn)
blueButton.addEventListener('click',blueBtn)