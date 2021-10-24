print("Hello world\n"*4 + 'I love Python\n'*4)

# Ask the user to input a month (1 to 12).
month = int(input('Enter a number of a month 1-12: '))
# Display the season of the month received :
# Spring runs from March (3) to May (5)
if month >= 3 and month <= 5 :
    print('Spring ')
# Summer runs from June (6) to August (8)
if month >= 6 and month <= 9 :
    print('Summer ')
# Autumn runs from September (9) to November (11)
if month >= 9 and month <= 11 :
    print('Autumn ')
# Winter runs from December (12) to February (2)
if month == 12 or month <= 2 :
    print('Winter')
else:
    print('no such a month')
    exit()