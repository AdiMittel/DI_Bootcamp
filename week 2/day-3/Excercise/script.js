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


function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`You name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
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

function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
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

function checkDriverAge() {
    if (driverAge > 18) {
        console.log('You are old enough to drive, Powering On.Enjoy the ride!');
    }
    else if (driverAge === 18) {
        console.log('Congratulation! this is your first year of driving!');
    }
    else {
        console.log('Sorry, you are too young to drive this car.Powering off');
    }
}

// checkDriverAge2(15)
// checkDriverAge2(18)
// checkDriverAge2(24)

function checkDriverAge2(age) {
    if (age > 18) {
        console.log('You are old enough to drive, Powering On.Enjoy the ride!');
    }
    else if (age === 18) {
        console.log('Congratulation! this is your first year of driving!');
    }
    else {
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
        if (i % 2 === 0) {
            console.log(`${i} is an even number`);
        } else {
            console.log(`${i} is an odd number`);
        }

    }
}

//------------------------------------------------------------------
//4
// let res = isDivisble()
// console.log('Sum is:',res);

function isDivisble() {
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i % 23 === 0) {
            console.log(`${i} is divided by 23!`);
            sum += i
        }

    }
    return sum
}
// isDivisble2(45)
// isDivisble2(23)

function isDivisble2(divisor) {
    let sum = 0
    for (let i = 0; i < 500; i++) {
        if (i % divisor === 0) {
            console.log(`${i} is divided by ${divisor}!`);
            sum += i
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
    if (item in amazonBasket) {
        console.log(`The item you were looking for exists!`);
    } else {
        console.log('The item you looked for is missing ,maybe next time..');
    }
}
//-------------------------------------------------------------------
//6
let Quarters = 0.25
let Dimes = 0.10
let Nickels = 0.05
let Pennies = 0.01

console.log(changeEnough([25, 20, 5, 0], 10.25));
console.log(changeEnough([25, 20, 5, 0], 4.25));
function changeEnough(array, total) {
    let sum = 0
    for (let i = 0; i < array.length; i++) {
        switch (i) {
            case 0:
                sum += array[i] * Quarters
                break;
            case 1:
                sum += array[i] * Dimes
                break;
            case 2:
                sum += array[i] * Nickels
                break;

            default:
                sum += array[i] * Pennies
                break;
        }
    }
    if (sum >= total) {
        return true
    } else {
        return false
    }

}

//-------------------------------------------------------------------
// //7
let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ['banana', 'orange', 'apple']

function myBill() {
    let bill = 0
    for (let i = 0; i < shoppingList.length; i++) {
        if (Object.keys(stock).includes(shoppingList[i])) {
            // console.log(stock[shoppingList[i]])
            if (stock[shoppingList[i]] !== 0) {
                for (let j = 0; j < Object.keys.length; j++) {
                    if (Object.keys(prices).includes(shoppingList[i])) {
                        bill += prices[shoppingList[i]]
                        Object.values(stock[shoppingList[i]]) - 1
                        stock[shoppingList[i]] -= 1
                    }
                }
            }
        }
    }
    console.log('The bill is:', bill);
    console.log(stock);
}
// myBill()

//----------------------------------------------------------------------
//8
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).

// tipCalculator()

function tipCalculator() {
    let bill = +prompt('How much is your bill?')
    let tip = 0
    let total = 0
    if (bill < 50) {
        tip += bill * 0.20
        total += tip + bill
        console.log(`Your bill is ${bill} so for tip you need to add ${tip} total of ${total}`);
    }
    else if (bill > 50 && bill < 200) {
        tip += bill * 0.15
        total += tip + bill
        console.log(`Your bill is ${bill} so for tip you need to add ${tip} total of ${total}`);
    } else {
        tip += bill * 0.1
        total += tip + bill
        console.log(`Your bill is ${bill} so for tip you need to add ${tip} total of ${total}`);
    }
}

//------------------------------------------------
//9




function hotelCost() {
    let nightsNum = +prompt('How many nights whould you like to stay?')
    let price = 140

    while (!nightsNum > 0) {
        nightsNum = +prompt('How many nights whould you like to stay?')
    }
    price *= nightsNum
    return price;

}
//-------------



function planeRideCost() {
    let planePrice = 0
    let destination
    do {
        destination = prompt('What destination you\'d like to go?').toLowerCase()

    } while (typeof destination !== 'string');
    switch (destination) {
        case 'london':
            planePrice += 183
            break;
        case 'paris':
            planePrice = 220
            break;

        default:
            planePrice = 300
            break;
    }
    return planePrice
}
//------------

function carRentalCost() {
    let rentalDays
    let price = 40
    do {
        rentalDays = Number(prompt('How many days would you like to rent a car?'))
    } while (isNaN(rentalDays));
    
    if(rentalDays >= 10){
        price *= rentalDays
        price-= price*0.2
        
    }else{
        price *= rentalDays
    }

    return price;

}

//-----------
function totalVacationCost(){ 
    let total = `The price of the hotel is ${hotelCost()}$,plane price is ${planeRideCost()}$ and the car rental price is ${carRentalCost()}$`
    return total
}
let res = totalVacationCost()
console.log(res);