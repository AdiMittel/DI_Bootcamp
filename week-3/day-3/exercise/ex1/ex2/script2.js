// <!-- Create a draggable square/box element in your HTML file.
// In your javascript file add the functionality which will allow you
//  to drag the square/box and
//  drop it into a larger box. -->

let drag = document.getElementById('drag')
let dropZone = document.getElementById('dropzone')

drag.addEventListener('dragstart',startDragging)

function startDragging (event) {
    event.dataTransfer.setData("text/plain",event.target.id)
}
addTheListeners()
function addTheListeners(){
    dropZone.addEventListener("dragover", draggingOver)
	dropZone.addEventListener("drop", dropping)
}

function draggingOver (event) {
	event.preventDefault();
}

function dropping(event) {
    event.preventDefault();
	// console.log(event.target)
	// 1. retrieve the element that we want to srop
	let elementToDrop = event.dataTransfer.getData("text/plain")
	// 2. append the element on the drop zone
	let elemNode = document.getElementById(elementToDrop)
    elemNode.classList.remove("startDragging");
	event.target.appendChild(drag)
}