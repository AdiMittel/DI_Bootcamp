// 1. Write a JavaScript for loop that will iterate from 0 to 15.
//  For each iteration, it will check if the current number is odd or even,
//   and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

for (let i = 0; i <= 15; i++) {
    let num = i;
    if(i%2 === 0){
        console.log(i,'is an even number!');
    }else{
        console.log(i,'is an odd number!');
    }
    
}

// 1. Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not,
//  change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

// let names= ["john", "sarah", 23, "Rudolf",34]
// for (let i = 0; i < names.length; i++) {
//     if(typeof names[i] === 'string'){
//         console.log(names[i]);
//         names[i][0] = names[i][0].toUpperCase
//         // for(let j = 0 ; j < names[i].length ; j++){
//         //     names[i][0] = names[i][0].toUpperCase()
//         // }
//         console.log(names[i]);
//     }
    
    
// }

// 1. Loop over this array, and add to the array the word in plural
//  ("s" at the end) of every fruit

let shopping = ["apple", "pear", "melon", "banana"];

for (let i = 0; i < shopping.length; i++) {
    shopping[i]+='s'
}
console.log(shopping);
// -----------------------------------

let prices = [23, 15, 34, 10];
let pricesSum = 0;
for (let i = 0; i < prices.length; i++) {
    pricesSum += prices[i]
}
console.log('Total price is:',pricesSum);