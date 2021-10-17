let names = ["John", "Lola", "Tom"];
// 1. Create a function that adds the name of each students to 
// a paragraph
// 2. each paragraph needs to be background yellow, font-size 25px
// 3. Add the 3 paragraph to the div already on the page
let content = document.querySelector('.container')
for (let i = 0; i < names.length; i++) {
    let para = document.createElement('p')
    para.innerText = names[i]
    content.appendChild(para)
}
console.log(content);