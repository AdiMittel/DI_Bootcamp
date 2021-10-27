# Create a function that accepts a number between 1 and 100 and generates
#  another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message,
#  otherwise show a fail message and display both numbers.
import random

def compare_numbers(num):
    rand_num = random.randint(1,10)
    if num == rand_num:
        print(f'Success! we chose the same number! {rand_num} {num}')
    else:
        print(f'Numbers are not the same! {rand_num} {num}')

compare_numbers(5)