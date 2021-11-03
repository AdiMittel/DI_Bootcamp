# list_1 = [1,2,3]
# list_2 = [4,5,6]

# list_1+=list_2
# print(list_1)

#------------------------

# num_1=input('Enter first number ')
# num_2=input('Enter second number ')
# num_3=input('Enter third number ')

# if num_3 > num_2 and num_3 > num_1:
#     print(num_3)
# elif num_2 > num_1 and num_2 > num_3:
#     print(num_2)
# else:
#     print(num_1)

#-------------------------------

# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for letter in alphabet:
#     if letter in 'aeiou':
#         print(letter,'is vowel')
#     else:
#         print(letter,'is consonant')

#---------------------------------------------------

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# user_name = input('what is your name?').title()

# if user_name in names:
#     print('index is: ', names.index(user_name))
# else:
#     print('This name is not exist..')

#-----------------------------------------------------

# user_words = []
# for i in range(0,7):
#     word_input = input('Enter a word: ')
#     user_words.append(word_input)
# letter = input('Please enter a single character: ')
# for word in user_words:
#     if letter in word:
#         print('The char is in inedx: ', word.index(letter))
#     else:
#         print('Character was not found!')

#-----------------------------------------------------------

# numbers=list(range(1,1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

#-------------------------------------------------------------------------------

# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')