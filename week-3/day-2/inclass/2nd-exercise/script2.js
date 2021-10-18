
// 3. Each button should have an "click" event listener that 
// changes the background color of the document,  to the color of the button
//  (do it directly in the JS)

let colors = ["blue", "yellow", "green", "pink"];
let container = document.querySelector('#container')

for (let i of colors) {
    let newBtn = document.createElement('button')
    newBtn.innerText = i
    newBtn.style.color = i
    newBtn.style.height = '50px'
    newBtn.style.width = '50px'
    newBtn.addEventListener('click',changeColor)
    container.appendChild(newBtn)
}

function changeColor(event) {
    let body = document.querySelector('body')
    body.style.backgroundColor = event.target.textContent
}