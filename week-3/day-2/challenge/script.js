// Get the value of each of the inputs in the HTMLfile when the button is clicked.
let inputs = document.querySelectorAll('input')
let values = []
for (let i = 0; i < inputs.length; i++) {
    values += inputs[i]
    console.log(values);
}
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.