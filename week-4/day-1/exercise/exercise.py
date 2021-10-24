# 1
# print('Hello World \n'*4)
#-----------------------------------------------------------------
# #2
# # (99^3) * 8
# print('(99^3) * 8 =',(99**3)*8) 
#---------------------------------------------------------------------
# #3
# print(5 < 3) #= False
# print(3 == 3) #= True
# print(3 == "3") #= False
# # print("3" > 3) #error
# print("Hello" == "hello") #False
#--------------------------------------------------------------
# #4
# # Create a variable called computer_brand which value is the brand name of your computer.
# # Using the computer_brand variable print a sentence that states the following:
# #  "I have a <computer_brand> computer".

# computer_brand = 'Lenovo'
# print('I have a {} computer'.format(computer_brand))
#-------------------------------------------------------------------
# #5
# # Create a variable called name, and set it’s value to your name.
# name = 'Adi'
# # Create a variable called age, and set it’s value to your age.
# age = 22
# # Create a variable called shoe_size, and set it’s value to your shoe size.
# shoe_size = 44
# # Create a variable called info and set it’s value to an interesting sentence about yourself.
# info = "I love the beach"
# #  The sentence must contain all the variables created in parts 1, 2 and 3.
# # Have your code print the info message.
# # Run your code
# print('My name is {}, i\'m {} years old,My shoes size is:{}, and something about me is that:{}'.format(name,age,shoe_size,info))
#---------------------------------------------------------------------------------------------
#6
# Create two variables, a and b.
# Each variables value should be a number.
# If a is bigger then b, have your code print Hello World.
# a = 14
# b = 8
# if a > b :
#     print('Hello world')
#--------------------------------------------------------------------------------------
#7
# Write code that asks the user for a number and determines whether this number is odd or even.
# num = int(input('Enter a number'))

# if num % 2 == 0:
#     print('This is an even number!')
# else:
#     print('this is an odd number!')

#-------------------------------------------------------------------------------------
#8
# Write code that asks the user for their name and determines whether or not you have the same name,
#  print out a funny message based on the outcome.
# user_name = input('Enter your name: ')
# if user_name == name:
#     (print('Hey {},You have such a beatiful name because its my name too!'.format(user_name)))
# else:
#     print('Hey {},You\'re name sucks'.format(user_name))
#--------------------------------------------------------------------------------------
#9
# Write code that will ask the user for their height in inches.
height_inches = int(input('how tall are you? (by inches) '))
height_cm = height_inches*2.54
# If they are over 145cm print a message that states they are tall enough to ride.
if height_cm >= 145:
    print('You are Tall enought for the ride. Enjoy!')
# If they are not tall enough print a message that says they need to grow some more to ride.
else:
    print('Take some growing pill if you want to get on this ride.. ')
