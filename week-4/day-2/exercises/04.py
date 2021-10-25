# Recap – What is a float? What is the difference between an integer and a float?

# float is a number with a follow decimal dot. integer is a full number without decimal dot and numbers after it

# Can you think of another way to generate a sequence of floats?

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 
# (don’t hard-code the sequence).
my_list = []
for num in range(1,6,1):
    my_list.append(num)
    my_list.append(num+0.5)
print(my_list)