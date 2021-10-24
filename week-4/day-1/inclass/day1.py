# Ask the user for a number between 1 and 100
num = int(input('Enter a number between 1-100'))
# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.
if num % 3 == 0 and num % 5 == 0:
    print('BuzzFizz')

# If the number is a multiple of three, print "Fizz"
elif num % 3 == 0:
    print('Fizz')

# If the number is a multiple of five, print "Buzz".
elif num % 5 == 0:
    print('Buzz')

