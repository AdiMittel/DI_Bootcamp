# A movie theater charges different ticket prices depending on a person’s age.
tickets = input('What are your ages? ').split(' ')

total_price = 0
for age in tickets:
    age = int(age)
# if a person is under the age of 3, the ticket is free.
    if age <= 3 :
        continue
# if they are between 3 and 12, the ticket is $10.
    elif age > 3 and age <= 12:
        total_price += 10
# if they are over the age of 12, the ticket is $15.
    else :
        total_price+=15
print('Total cost of the movie tickes is:{}'.format(total_price))

# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted
#  for people between the ages of 16 and 21.

ages = input('Enter ages to see if permitted to see the movie ').split(' ')   
for x in ages :
    x = int(x)
    if x >= 16 and x <= 21 :
        print(x,'Enjoy the movie!')
    else:
        print(x,'You are not allowed to watch that movie..')


# Write a program that asks every user for their age, 
# and prints a list of the teens who are permitted to watch the movie.
