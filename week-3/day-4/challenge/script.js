let list = document.querySelector('.listTasks')
let input = document.querySelector('#myInput')
let submit = document.querySelector('.addBtn')
let newLi
let checkBox
// let form = document.querySelector('.input')
let form = document.getElementById('form')
let listTasks = ['Breakfast','Work']

form.addEventListener('submit',addTask)

let newUl = document.createElement('ul')
newUl.classList.add('myUl')
list.appendChild(newUl)

function addTask(e) {
    e.preventDefault();
    listTasks.push(input.value)
    for (let i = 0; i < listTasks.length; i++) {
        newLi = document.createElement('li')
        checkBox = document.createElement('input')
        newLi.classList.add('line')
        checkBox.setAttribute('type','checkbox')
        checkBox.addEventListener('click',toggleDone)
        checkBox.classList.add('box')
        newLi.textContent = listTasks[i]
        
    }
    newLi.appendChild(checkBox)
    newUl.appendChild(newLi)
    input.value = ''
}

// submit.addEventListener('submit',clearInput)

function clearInput(event) {
    input.setAttribute('placeholder','')
}

function toggleDone (e) {
    if(this.checked){
        console.log(e.target.parentElement);
        e.target.parentElement.style.textDecoration = 'line-through'
    }else{
        e.target.parentElement.style.textDecoration = 'none'
    }
}