# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
family_total_price = 0
for keys,values in family.items() :
    if values < 3:
        continue
    elif values >= 3 and values <= 12:
        price = 10
        family_total_price += 10
    else :
        price = 15
        family_total_price += 15
    print(keys,values,price)
print('Family total price is:',family_total_price) 
# How much does each family member have to pay ?
# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the
#  provided family variable (Hint: ask the user for names and ages and add them
#   into a family dictionary that is initially empty).
