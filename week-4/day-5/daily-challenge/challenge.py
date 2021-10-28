# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

def get_input():
    user_input = input('Enter a string seperated by comma\'s ')
    return user_input

def sort_input():
    input_str = get_input()
    input_list = input_str.split(',')
    print(input_list)
    input_list = sorted(input_list)
    input_str = ','.join(input_list)
    print(input_str)

sort_input()