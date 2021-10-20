let colorsBar = document.querySelector('.color')
let colors = [ "blue",
"lightBlue",
"Aqua",
"Aquamarine",
"Azure",
"Brown",
"Chocolate",
"Black",
"BlanchedAlmond",
"Chartreuse",
"BlueViolet",
"Brown",
"yellow",
"Orange",
"Gray"]

for (let i = 0; i <colors.length; i++) {
    let newDiv = document.createElement('div')
    newDiv.classList.add('colors')
    newDiv.classList.add(colors[i])
    newDiv.style.backgroundColor = colors[i]
    newDiv.addEventListener('click', getColor)
    colorsBar.appendChild(newDiv)
}

let board = document.querySelector('.paintArea')
let newDivs
for (let i = 0; i < 1440; i++) {
    newDivs = document.createElement('div')
    newDivs.classList.add('plain')
    newDivs.style.border = '1px black solid'
    newDivs.addEventListener('mousedown',changeColor)
    board.appendChild(newDivs)
}
let currColor
function getColor(){
    currColor=this.style.backgroundColor;
}

function changeColor(event) {
    event.target.style.backgroundColor = currColor
}

function clearBoard() {
    // newDivs.style.backgroundColor = 'White'
    let clearDivs = document.querySelectorAll('.plain')
    for (let i = 0; i < 1440; i++) {
        clearDivs[i].style.backgroundColor = "white"
    }
}