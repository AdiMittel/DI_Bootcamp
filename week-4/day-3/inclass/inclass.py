# my_dict = {'first_name':'Toby' ,
# 'last_name':'Ziegler',
# 'birth_date' : '31.10.2012'}

# print(my_dict['last_name'])

# print(my_dict.items())


# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# # for key in sample_dict:
# #     history = sample_dict[key]

# # print(history)
# print(sample_dict['class']['student']['marks']['history'])
# sample_dict['class']['student']['marks']['history'] = 100
# print(sample_dict['class']['student']['marks']['history'])
# print(sample_dict['class']['student']['marks'])
# del sample_dict['class']['student']['marks']['physics']
# print(sample_dict['class']['student']['marks'])


sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys_to_remove = ["name", "salary"]

for key in keys_to_remove :
    del sample_dict[key]
print(sample_dict)