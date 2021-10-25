# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {12,16,20}
# Add two new numbers to the set.
my_fav_numbers.add(15)
my_fav_numbers.add(55)
print(my_fav_numbers)
# Remove the last number.
my_fav_numbers.pop()
print(my_fav_numbers)
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers = {22,33,44}
print(friend_fav_numbers)
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
our_fav_numbers = friend_fav_numbers |(my_fav_numbers)
print(our_fav_numbers)