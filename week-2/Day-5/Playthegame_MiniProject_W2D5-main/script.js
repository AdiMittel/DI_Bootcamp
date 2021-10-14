function playTheGame() {
    if (confirm()) {
        enterNumber();
    } else {
        console.log('No problem,Goodbye!');
    }
}

function enterNumber() {
    let num = Number(prompt('Enter a number:'))
    do {
        if(isNaN(num))
        num = Number(prompt('Enter a valid NUMBER!:'))
    } while (isNaN(num));
    
    if (isNaN(num)) {
        console.log('Sorry Not a number, Goodbye');
    } else {
        if (num > 10 || num < 0) {
            console.log('Not a good number,try again!');
            
        } else {
            checkNumbers(num)
        }
    }
    
}

function checkNumbers(number) {
    for (let i = 1; i <=3; i++) {
        let computerNumber = 5
        //Math.floor(Math.random() * 10)
        if (number === computerNumber) {
            console.log(computerNumber,number);
            alert('You won!');
            break
        }
        if (i ===3) {
            alert('Out of guesses')
            break
        }else if(number > computerNumber){
            console.log(computerNumber,number);
            number = Number(prompt('Your number is bigger then the computer’s, guess again '));
        }else{
            console.log(computerNumber,number);
           number = Number(prompt('Your number is smaller then the computer’s, guess again'));

        }
        
    }
    
}