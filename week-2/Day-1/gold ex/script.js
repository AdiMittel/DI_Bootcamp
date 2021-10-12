'use strict'
//Exercise 1

// let me = ["my","favorite","color","is","blue"]
// console.log(me.join());

//Exercise 2 *not finished

// let str1 = "mix" 
// let str2 = "pod"
// // str1.slice(1)
// let newStr=str1.concat(' '+str2)

// console.log(newStr);

//Exercise 3

let operator = prompt('Choose the operator you\'d like to use: +, -, *, /')

if (operator === '+'){
    let num1 = +prompt('Enter a number:')
    let num2 = +prompt('Enter a number:')
    let result=num1+num2
    alert('Result: '+result)
}
else if (operator === '-'){
    let num1 = +prompt('Enter a number:')
    let num2 = +prompt('Enter a number:')
    let result=num1-num2
    alert('Result: '+result)
}
else if (operator === '*'){
    let num1 = +prompt('Enter a number:')
    let num2 = +prompt('Enter a number:')
    let result=num1*num2
    alert('Result: '+result)
}
else if (operator === '/'){
    let num1 = +prompt('Enter a number:')
    let num2 = +prompt('Enter a number:')
    let result=num1/num2
    alert('Result: '+result)
}
else{
    alert('Valid action!')
}



    


