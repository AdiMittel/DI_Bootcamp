// Ask the user which language they speak.
// Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”
// Create a few conditions :
// If the user speaks French : display “Bonjour”
// If the user speaks English : display “Hello”
// If the user speaks Hebrew : display “Shalom”
// If the user doesn’t speak any of these 3 languages:
// display ‘01110011 01101111 01110010 01110010 01111001’

// let language = prompt('Choose the language you speak').toLowerCase()
// switch (language) {
//     case 'english':
//         console.log('Hello');
//         break;
//     case 'french':
//         console.log('Bounjour');
//         break;
//     case 'hebrew':
//         console.log('Shalom');
//         break;

//     case 'arabic':
//         console.log('Salam');  
//         break;  
//     default:
//         console.log('01110011 01101111 01110010 01110010 01111001');
//         break;
// }

// Ask the user for their grade.
// If the grade is bigger than 90, console.log “A”
// If the grade is between 80 and 90 (included), console.log “B”
// If the grade is between 70(included) and 80 (included), console.log “C”
// If the grade is lower than 70, console.log “D”

let grade = parseInt(prompt('Enter your grade:')) 

if (grade >= 90){
    console.log(grade);
    console.log('you got an A');
}
else if(90 > grade && grade >= 80){
    console.log(grade);
    console.log('Your got a B');
}
else if(80 > grade && grade >= 70){
    console.log('You got a C');
    console.log(grade);
}
else{
    console.log('You got the D');
    console.log(grade);
}

