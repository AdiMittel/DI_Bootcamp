# Given a list, use a loop to print out every element which has an even index.
my_list = [0,1,2,3,4,5,6,7,8,9]

for i in my_list :
    if my_list.index(i) % 2 == 0 :
        print(i)
    else :
        continue
