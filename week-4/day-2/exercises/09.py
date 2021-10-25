# Ask the user to input their favorite fruit(s) (one or several fruits).
user_fruits = input('Enter your favorite fruits(if you got more than 1 seperate them by single space): ')
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. 
#"apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
user_fruits = user_fruits.split(' ')
# Now that we have a list of fruits, ask the user to input a name of any fruit.
search_fruit = input('Give a name of a fruit to see if you like it: ')
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
if search_fruit in user_fruits:
    print('It\'s one of your favorite fruits')
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
else:
    print('You chose a new fruit,I hope you enjoy it!')

