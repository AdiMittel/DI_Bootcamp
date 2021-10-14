//Logics:
//

// Prompt the user for several words (separated by commas).
// Put the words into an array.
let words = prompt('Enter few words seperated by a comma ","')
function wordsToArray(str) {
    str = words.split(',')
    return str;
}

let res = wordsToArray(words)
console.log(res);
// Console.log the words one per line, in a rectangular frame as seen below.
let longStr = findLongestStr(res)
function findLongestStr(array) {
    let longestStr = 0
    for (let i = 0; i < array.length; i++) {
        if(array[i] > longestStr){
            longestStr = array[i]
        }
    }
    return longestStr
}
console.log(longStr);

printFramedWords()

function printFramedWords(str){
    let row = ''
    for (let i = 0; i < longStr.length +4; i++) {
        
    }
    console.log(row);
        
}


// Check out the Hints and Requirements below.