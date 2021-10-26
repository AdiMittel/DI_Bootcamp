users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
num_list = []
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# disney_users_A={}
# for i in range(0,len(users)):
#     num_list.append(i)
# disney_users_A = dict(zip(users,num_list))
# print(disney_users_A)
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B={}
for i in range(0,len(users)):
    num_list.append(i)
disney_users_B = dict(zip(num_list,users))
# print(disney_users_B)
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
disney_users_C = {}
for i in range(len(users),0):
    num_list.append(i)
disney_users_C = dict(zip(reversed(users),num_list))
print(disney_users_C)