// Create an array which value is the planets of the solar system.
let planets = ['Earth', 'Mars', 'Jupiter']
// let earht = document.querySelector('.Earth')
// let mars= document.querySelector('.Mars')
// let jupiter = document.querySelector('.Jupiter')
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".


for (let i = 0; i < planets.length; i++) {
    let disPlanets = document.createElement('div')
    disPlanets.setAttribute('class', 'planet')
    let planetList = document.querySelector('.listPlanets')
    disPlanets.classList.add(planets[i])
    disPlanets.innerText=planets[i]
    disPlanets.style.fontSize = '20px'
    disPlanets.style.display = 'grid'
    planetList.appendChild(disPlanets)


}



let myPlanets = document.querySelectorAll('.planet')


// Each planet should have a different background color. (Hint: add a new class to each planet).

document.querySelector('.Earth').style.backgroundColor = "blue"
document.querySelector('.Mars').style.backgroundColor = "orange"
document.querySelector('.Jupiter').style.backgroundColor = "pink"

// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?