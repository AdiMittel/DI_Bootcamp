# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made ,
#  such as I made your tuna sandwich.

sandwich_orders = ['Avocado','Egg','Tuna','Cheese']
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print('I made a ' + current_sandwich+'sandwich')
    finished_sandwiches.append(current_sandwich)
print()
for sandwich in finished_sandwiches:
    print(sandwich + ' is done')