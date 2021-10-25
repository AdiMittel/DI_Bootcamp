# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
basket.remove('Banana')
# Remove “Blueberries” from the list.
basket.remove('Blueberries')
# Add “Kiwi” to the end of the list.
basket.append('Kiwi')
# Add “Apples” to the beginning of the list.
basket.append('Apples')
# Count how many apples are in the basket.
apples_count = 0
for i in basket :
    if i == "Apples":    
        apples_count+=1   
print('I have {} apples in my baket'.format(apples_count))
    
# Print(basket)
print(basket.clear())