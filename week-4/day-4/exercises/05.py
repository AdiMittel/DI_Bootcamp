# Write a function called make_shirt() that accepts a size and the text of a
#  message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt 
# and the message printed on it.
def make_shirt(size='Large',txt='I love Python!'):
    if size != 'Medium' and size != 'Large':
        txt = 'I miss JS!'
    print(f'This T-shirt is {size} size and written on it {txt}.')
make_shirt('Medium')
# Call the function make_shirt() using positional arguments to make a shirt.
# Modify the make_shirt() function so that shirts are large by default with 
# a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
#  and a shirt of any size with a different message.
# Bonus: Call the function make_shirt() using keyword arguments