
// let nav = document.querySelector("#navBar")
// nav.setAttribute("id","socialNetworkNavigation")

// let inUl = document.getElementsByTagName("ul")[0]

// let newLi = document.createElement("li")

// let newA = document.createElement("a")
// newA.setAttribute("href","")
// newA.innerText = "logout"
// newLi.appendChild(newA)
// inUl.appendChild(newLi)



// console.log(inUl.firstElementChild.textContent);
// console.log(inUl.lastElementChild.textContent)

//-------------------------------------------------------------------------------
// let ulAccess = document.querySelector('.list')
// let name = ulAccess.lastElementChild
// name.innerText = 'Richard'

// // Change each first name of the two <ul>'s to your name.

// let inUl = document.querySelectorAll('.list')
// let newLi = document.createElement('li')
// newLi.innerText = 'Hey students'
// for (const x of inUl) {
//     x.firstElementChild.textContent = 'Adi'
// }
// for (const y of inUl) {
//     let newLi = document.createElement('li')
//     newLi.innerText = 'Hey students'
//     y.appendChild(newLi)
// }

// let as = document.body.children[2]
// as.removeChild(as.children[1])


// for (const x of inUl) {
//    x.classList.add("class","student_list")
// }
// let firstUl = document.body.children[1].classList.add('class','University','Atterndance')

//------------------------------------------------------------------------
// Add a “light blue” background color and some padding to the <div>.
let title = document.querySelector("div")
title.style.backgroundColor = 'lightblue'
// Do not display the first name (John) in the list.
let firstName = document.querySelector('li')
firstName.style.display = 'none'
// Add a border to the second name (Pete).
let secondName = document.getElementsByTagName('li')[1]
secondName.style.border ='black solid 2px'
// Change the font size of the whole body.
let allBody = document.querySelector('body')
allBody.style.fontSize = "15px"
// Bonus: If the background color of the div is “light blue”,
//  alert “Hello x and y” (x and y are the users in the div).