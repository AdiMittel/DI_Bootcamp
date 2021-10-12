// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so:
//  “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”,
//  “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

// let colors = ['yellow', 'blue', 'red', 'purple'];
// let suffix = ['st', 'nd', 'rd', 'th']

// for (let i = 0; i < colors.length; i++) {
//     for (let j = 0; j < suffix.length; j++) {
//         if (j === i) {
//             switch (i) {
//                 case 0:
//                     console.log(`my ${i+1+suffix[j]} color is ${colors[i]}`);
//                     break;
//                 case 1:
//                     console.log(`my ${i+1+suffix[j]} color is ${colors[i]}`);
//                     break;
//                 case 2:
//                     console.log(`my ${i+1+suffix[j]} color is ${colors[i]}`);
//                     break;

//                 default:
//                     console.log(`my ${i+1+suffix[j]} color is ${colors[i]}`);
//                     break;
//             }
//         }
//     }
// }


//------------------------------------------------------
//2
let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
for (let i = 0; i < people.length; i++) {


}

// Write code to replace “James” to “Jason”.
for (let i = 0; i < people.length; i++) {
    if (people[i] === 'James') {
        people[i] = 'Jason'
    }
}
console.log(people);

// Write code to add your name to the end of the people array.
people.push('Adi')
console.log(people);

// Using a loop, iterate through the people array and console.log each person.
// Using a loop, iterate through the people array and after you 
//console.log “Jason” exit the loop.
for (let i = 0; i < people.length; i++) {
    if (people[i] === 'Jason') {
        console.log(people[i]);
        break;
    } else {
        console.log(people[i]);
    }

}

// Write code to make a copy of the people array using slice. 
//The copy should NOT include “Mary” or your name.
makeCopy()
function makeCopy() {
    let persons = ["Greg", "Mary", "Devon", "Jason", "Adi"]
    let newArr;
    for (let i = 0; i < persons.length; i++) {
        switch (persons[i]) {
            case 'Mary':
                newArr += persons.splice(i, 1)
                break;
            case 'Adi':
                newArr = persons.splice(i, 1)
                break;

            default:

                break;
        }

    }
    console.log(persons);
}

// Write code that console.logs Mary’s index. take a look at indexOf on google.


for (let i = 0; i < people.length; i++) {
    if (people[i] === 'Mary') {
        console.log('Mary\'s index is', i);
    }
}

// Write code that gives the indexOf “Foo” (this should return -1).
let indexOf = -1;
for (let i = 0; i < people.length; i++) {
    switch (people[i]) {
        case 'foo':
            indexOf = i
            break;

        default:
            break;
    }
}
console.log('Index is', indexOf);


// Why does it return -1
// Create a variable called last which value is the last element of the array.
let last = people[people.length - 1]
// for (let i = 0; i < people.length; i++) {
//     last = people[i] 

// }
console.log(last);



// Hint: What is the relationship between the index of the last element in the
// array and the length of the array?
// the index of the array will be the length -1.

//-----------------------------------------------------------------------
//3
//Prompt the user for a number,
// while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)

// let number = +prompt('Enter a number:');
// while (number < 10) {
//     number = +prompt('Enter a number:');
// }
//------------------------------------------------------------------------
//4
// Given the object above where the key is the students name and the value is
//  the country they are from.
let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
// Prompt the student for their name :
// If the name is in the object, console.log the name of the student and
//  the country they come from.
// let name = prompt('What\'s your name?')
// let country;
// if(Object.keys(guestList).indexOf(name)!=-1){
//     console.log(`Hi im ${name},and im from ${guestList[name]}`);
// }
// else{
//     console.log('Hi! i\'m a guest!')
// }


// console.log(guestList);
// example: "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if ... in
// If the name is not in the object, console.log: "Hi! I'm a guest."

//---------------------------------------------------------------
//5
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).

let family = {
    dad: 'Yossi',
    mom: 'Rivka',
    child1: 'Dan',
    child2: 'Tomer',
    dog: 'Shoko'
};

for (let i = 0; i < (Object.keys(family).length); i++){
    console.log(Object.keys(family)[i])
    
}
for (let i = 0; i < (Object.keys(family).length); i++){
    console.log(Object.values(family)[i]);
    
}

//------------------------------------------------
//6
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

  for (let i = 0; i < (Object.keys(details).length); i++){
    console.log(Object.keys(details)[i])
    console.log(Object.values(details)[i]);
}
//----------------------------------------------------------
//7
// A group of friends have decided to start a secret society. 
//The society’s name will be the first letter of each of their names sorted in
// alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
let groupName='';
for (let i = 0; i < names.length; i++) {
    groupName+=names[i][0]
    
}
console.log('The group name is:',groupName);
