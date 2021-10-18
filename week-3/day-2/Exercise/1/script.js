let body = document.querySelector('body')
// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.

let article = document.querySelector('article')
console.log(article);
article.lastElementChild.remove()

// Add an event listener which will change the background color of the h2 tag
//  from the DOM when clicked on.

let headline2 = document.querySelector('h2')
headline2.addEventListener('click',changeBackground)

// Set the font size of the h1 tag to a random pixel size between 0 to 100.
let headline1 = document.querySelector('h1').style.fontSize = Math.floor(Math.random() * 100)+'px'

// (Check out this documentation)
// Add an event listener which will hide the h3 when it’s clicked on 
// (use the display property).
document.querySelector('h3').addEventListener('click',hideElement)

// Add a <button> to the HTML file, that when clicked on,
//  should make the text of all the paragraphs, bold.
let newButton = document.createElement('button')
newButton.innerText = 'Bold'
newButton.addEventListener('click',boldParagraphs)
body.appendChild(newButton)
// When the “Submit” button of the form is clicked:
let submit = document.querySelector('#submit')
let inputs = document.querySelectorAll('input')
// get the values of the input tags



// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// When you hoover on the 2nd paragraph, it should fade out
//  (Check out “fade css animation” on Google)

function changeBackground(event){
    let body = document.querySelector('body')
    body.style.backgroundColor = 'red'
}

function hideElement(event) {
    event.target.style.display = 'none'
}
function boldParagraphs(event){
   let paragraphs=document.getElementsByTagName('p')
   for (let i of paragraphs) {
       i.style.fontWeight = 'bold'
   }
   
}