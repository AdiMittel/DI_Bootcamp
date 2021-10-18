// Create a function called getBold_items() that takes no parameter. This function should collect
//  all the bold items inside the paragraph.
function getBold_items() {
    let isBold = document.getElementsByTagName('strong')
    return isBold
}
getBold_items()
// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
    
    for (let i of getBold_items()) {
        i.style.backgroundColor = 'blue'
    }
}

// Create a function called return_normal() that changes the color of all the bold text back to black.
function return_normal() {
    getBold_items()
    for (let i of getBold_items()) {
        i.style.backgroundColor = 'white'
    }
}
let parag = document.querySelector('p')

for (let j = 0; j < 2; j++) {
    j === 0 ? parag.addEventListener('mouseover',highlight) : parag.addEventListener('mouseout',return_normal);
    
}



// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph),
//  and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph)