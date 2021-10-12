//Exercise 1

// let x = 6
// let y = 8

// if (x>y){
//     console.log('X is the Biggest number:',x);
// }else{
//     console.log('Y is the biggest number:',y);
// }


// //Exercise 2 

// let newDog = 'Chihuahua'

// console.log('Length of the word is:',newDog.length);

// console.log(newDog.toLowerCase());
// console.log(newDog.toUpperCase());

// if(newDog === 'Chihuahua'){
//     console.log('I love Chiuahuas');
// }else{
//     console.log('I dont care,i prefer cats');
// }

// //Exercise 3

// let num = +prompt('Choose a number to see if odd or even:')
// if (num%2 === 0){
//     console.log(`${num} is an even number`);
// }else{
//     console.log(`${num} is an odd number`);
// }

// Exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000","meuser1"]

if (users.length === 0){
    console.log('No users online');
}
else if (users.length === 1){
    
    console.log(users[0],'is online');
}
else if (5 > users.length > 2){
    console.log(`${users[0]} and ${users[1]} are online`);
}else{
    console.log(`${users[0]},${users[1]} and ${users.length-2} more are online!`);
}