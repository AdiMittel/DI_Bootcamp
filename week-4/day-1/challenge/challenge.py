import random
shuff_string = []
# Using the input function, ask the user for a string. The string must be 10 characters long.
new_str = input('Make a string that is 10 characters long.. ')
# If it’s less than 10 characters, print a message which states “string not long enough”.
if len(new_str) < 10:
    print('string must be 10 characters long!')
    exit()
# If it’s more than 10 characters, print a message which states “string too long”.
elif len(new_str) > 10:
    print('string must be 10 characters long! ')
    exit()
# Then, print the first and last characters of the given text.
else:
    for i in new_str:
        print(i)
        shuff_string.append(i)
# Construct the string character by character: Print the first character, 
# then the second, then the third, until the full string is printed. 
random.shuffle(shuff_string)
# wap some characters around then print the newly jumbled string (hint: look into the shuffle method)
print(''.join(shuff_string))
