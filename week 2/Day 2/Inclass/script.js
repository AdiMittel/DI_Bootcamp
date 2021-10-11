let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

// userCart['lastName']='Smith'
// console.log(userCart);

// userCart['prices']['pear'] *=1.17
// console.log(userCart);

// let fruit = prompt('Choose fruit: banana,apple,pear').toLowerCase()
// console.log(`You chose ${fruit} price is: ${userCart['prices'][fruit]}`);


if (userCart['isUserSignedIn']){
	console.log(`You are signed in! username:${userCart['username']} password:${userCart['password']}`);
}else{
	alert('You need to sign in!')
}