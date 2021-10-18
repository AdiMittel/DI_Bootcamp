// Create an array which value is the planets of the solar system.
let planets = ['Earth', 'Mars', 'Jupiter']

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

document.querySelector('.Earth').style.backgroundColor = "blue"
document.querySelector('.Mars').style.backgroundColor = "orange"
document.querySelector('.Jupiter').style.backgroundColor = "pink"