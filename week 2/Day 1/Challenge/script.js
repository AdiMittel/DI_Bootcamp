let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

// Remove Banana from the array.
fruits.splice(0, 1)
console.log('lets remove banana',fruits);
// Sort the array in alphabetical order.
fruits.sort()
console.log('sort alphabetic',fruits);
// Add “Kiwi” to the end of the array.
fruits.push('kiwi')
console.log('lets add kiwi',fruits);
// Remove “Apples” from the array. Don’t use the same method as in part 1.
fruits.shift('Apple')
console.log('remove apple',fruits);
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
fruits.sort()
console.log('lest sort backwoards',fruits.reverse());
// At the end you should see this outcome:
// ["Kiwi", "Oranges", "Blueberries"]


//Exercise 2
// Access and then console.log “Oranges”.

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let oranges = moreFruits[1][1]
console.log('Oranges',oranges);
