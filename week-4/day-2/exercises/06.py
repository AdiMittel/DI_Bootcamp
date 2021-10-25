# Write a while loop that will continuously ask the user for their name,
#  unless the input is equal to your name.

my_name = 'Adi'
user_name = input('Enter your name ')
while user_name != my_name:
    user_name = input('Enter your name ')
print('Such a beatiful name you got there ;)')
