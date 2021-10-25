# Write a loop that asks a user to enter a series of pizza toppings,
#  when the user inputs ‘quit’ stop asking for toppings.
pizza_price = 10
topping_list = []
order = input('Enter the toppings you would like to add to the pizza(to stop enter "quit"): ')
topping_list.append(order)
pizza_price+=2.5
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
while order != 'quit' :
    order = input('Enter the toppings you would like to add to the pizza: ')
    if order == 'quit':
        continue
    topping_list.append(order)
    pizza_price += 2.5
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is 
# for top in topping_list:
#     pizza_price += 2.5
#     print(pizza_price)
# # (10 + 2.5 for each topping).
print(topping_list)
print('Pizza price is:',pizza_price)