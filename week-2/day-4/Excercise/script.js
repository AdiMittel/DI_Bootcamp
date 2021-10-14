//1
//I
// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you
// (ie. your name, age, hobbies ect…).
// Call the function.

// infoAboutMe()

 function infoAboutMe() {
     let name = 'Adi'
     let age = 22
     let hobbie = 'surfing'
     console.log(`my name is ${name} im ${age} years old and i like ${hobbie} on my free time`);
 }

//------------------------------------------------------------------
// II
// Create a function called infoAboutPerson(personName, personAge
//     , personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person
//  (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:


// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")


function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log( `You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
}

//----------------------------------------------------------------------
//III
// Add a parameter personHobbies to the function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies).
// The function should
// console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// console.log the person’s hobbies one by one (ie. loop through the array of hobbies).
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies){
    console.log(`You name is ${personName}, you are ${personAge}. years old, your favorite color is ${personFavoriteColor}`);
    console.log('Hobbies:');
    for (let i = 0; i < personHobbies.length; i++) {
        console.log(personHobbies[i]);
    }
}
//------------------------------------------------------------------------
//2
// Ask the user for their age, and save the value to a variable.
// Create a function called checkDriverAge()
//  that will notify the user if they are permitted to drive. They must be at least 18 to drive.
// if the user is too young, alert “Sorry, you are too young to drive this car.
//  Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On.
//  Enjoy the ride!”
// if the user just turned 18, alert
//  “Congratulations on your first year of driving. Enjoy the ride!”
// Call the function.
// Instead of using prompt to ask the user for their age, have the checkDriverAge()
//  function accept an argument age.
// let driverAge = +prompt('Enter your age:')

// checkDriverAge()

function checkDriverAge(){
    if(driverAge > 18){
        console.log('You are old enough to drive, Powering On.Enjoy the ride!');
    }
    else if(driverAge === 18){
        console.log('Congratulation! this is your first year of driving!');
    }
    else{
        console.log('Sorry, you are too young to drive this car.Powering off');
    }
}

// checkDriverAge2(15)
// checkDriverAge2(18)
// checkDriverAge2(24)

function checkDriverAge2(age){
    if(age> 18){
        console.log('You are old enough to drive, Powering On.Enjoy the ride!');
    }
    else if(age === 18){
        console.log('Congratulation! this is your first year of driving!');
    }
    else{
        console.log('Sorry, you are too young to drive this car.Powering off');
    }
}

//-------------------------------------------------------------------------
//3
// Create a function called checkNumber() that takes no parameter.
// In the function, loop through numbers 0 to 100.
// Add an if/else block
// If the number is even, console.log "the number <number> is even"
// Else, console.log "the number <number> is odd"
// Call the function

// checkNumber()

function checkNumber() {
    for (let i = 0; i <= 100; i++) {
        if(i%2 === 0){
            console.log(`${i} is an even number`);
        }else{
            console.log(`${i} is an odd number`);
        }

    }
}

//------------------------------------------------------------------
//4
// let res = isDivisble()
// console.log('Sum is:',res);

function isDivisble(){
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i%23===0){
            console.log(`${i} is divided by 23!`);
            sum+=i
        }
        
    }
    return sum
}
// isDivisble2(45)
// isDivisble2(23)

function isDivisble2(divisor){
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i%divisor===0){
            console.log(`${i} is divided by ${divisor}!`);
            sum+=i
        }
        
    }
    console.log(sum);
}
//--------------------------------------------------------------------------
//5
// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}
// checkBasket()
function checkBasket() {
    let item = prompt('Check if the item you look for is available!')
    if (item in amazonBasket){
        console.log(`The item you were looking for exists!`);
    }else{
        console.log('The item you looked for is missing ,maybe next time..');
    }
}
//-------------------------------------------------------------------
//6
let Quarters  = 0.25
let Dimes = 0.10
let Nickels = 0.05
let Pennies = 0.01

console.log(changeEnough([25, 20, 5, 0], 10.25)); 
console.log(changeEnough([25, 20, 5, 0], 4.25)); 
function changeEnough(array, total){
    let sum = 0
    for (let i = 0; i < array.length; i++) {
            switch (i) {
                case 0:
                    sum+=array[i]*Quarters
                    break;
                case 1:
                    sum+=array[i]*Dimes
                    break;
                case 2:
                    sum+=array[i]*Nickels
                    break;
            
                default:
                    sum+=array[i]*Pennies
                    break;
            }
        }
        if(sum >= total){
            return true
        }else{
            return false
        }
        
}
    
//----------------------------
// //7
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// Create the program explained above.

function tipCalculator(){
    let tip = 0
    let bill = +prompt()
    if (bill < 50) {
        tip+=bill*0.2
    }else if(bill > 50 || bill < 200){
        tip+=bill*0.15
    }else{
        tip+= bill*0.1
    }
    console.log(`The bill is ${bill},the tip is ${tip}. Total bill is ${bill+tip}`);
}
// tipCalculator()

//-----------------------------------------------------------------
//9
// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in
//  the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of
//  the hotel.
console.log(hotelCost());
function hotelCost(){
    let priceForNight = 140
    let totalPrice = 0
    let nightsCount = parseFloat(prompt('How many nights would you like to stay?')) 
    
    console.log(typeof nightsCount);
    // while(typeof nightsCount !== typeof 1){
    //     nightsCount = prompt('How many nights would you like to stay?')
    // }
    // totalPrice = nightsCount * priceForNight
    // return totalPrice
}

