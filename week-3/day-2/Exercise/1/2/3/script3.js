// Write a JavaScript program to calculate the volume of a sphere.
// Use the code below as a base:

let radius = document.getElementById('radius')
let height = document.getElementById('height')
let submit = document.getElementById('submit')



function calculate(){
    let volumeRes = (parseInt(radius.value)+parseInt(height.value))*2
    console.log(volumeRes);
}