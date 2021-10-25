# Given a list of names, write a program that asks every user for their age,
# if they are less than 16 years old remove them from the list.
# At the end, print the final list.
names_list = ['Adam','Daniel','John']
for name in len(names_list) :
    age = input('Enter age ')
    age = int(age)
    if age < 16 :
        print(name,age)
        names_list.remove(name)
        continue
    else:
        continue

print(names_list)