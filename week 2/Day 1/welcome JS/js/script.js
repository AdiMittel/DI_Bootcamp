let addressNumber = 13;
let addressStreet = " Rostchild ";
let country = "Israel ";

let globalAddress = addressNumber+ addressStreet+ country;
console.log('My address is:',globalAddress);

// 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

// 2. Display dog

// 3. Add to the array pets, the pet horse. Remove the pet cow

// 4. Display the array length

let pet = ['cat','dog','fish','rabbit','cow'];
console.log(pet);
console.log(pet[1]);

pet.pop();
console.log(pet);

pet.push('horse');
console.log(pet);

console.log(pet.length);
