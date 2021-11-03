members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]


class Family:
    def __init__(self, **kwargs):
        self.member = kwargs

    def born(self):
        members.append(self.member)
        print(f'Congrats for the new born! {self.member}')
        return self.member

    def is_18(self, name):
        for member in members:
            if name in member.values():
                if member['age'] >= 18:
                    return True
                else:
                    return False


# lastname = Family(name="Adi",age = 23,gender='male',is_child = True)
# lastname.born()
# print('is he over 18?',lastname.is_18('Adi') )
# ---------------------------------------------------------
incredible_family = [
    {'name': 'Bob', 'age': 45, 'gender': 'male', 'is_child': False,'power':'strong','incredible_name':'Mr. incredible'},
    {'name': 'Helen', 'age': 38, 'gender': 'female', 'is_child': False,'power':'flexible','incredible_name':'elastigirl'},
    {'name': 'Violet', 'age': 16, 'gender': 'female', 'is_child': True,'power':'invisible','incredible_name':'ghost girl'},
    {'name': 'Dash', 'age': 13, 'gender': 'male', 'is_child': True,'power':'fast','incredible_name':'Usain bolt'},
    {'name': 'john jackson', 'age': 2, 'gender': 'male', 'is_child': True,'power':'shape shifting','incredible_name':'jack jack'},
    
]


class TheIncredibles(Family):
    def __init__(self, **kwargs):
        super().__init__(self,**kwargs)
        incredible_family.append(kwargs)

    def use_power(self, name):
        for member in incredible_family:
            if name in member.values():
                if member['age'] >= 18:
                    print(member['power'])
                else:
                    print(f'{member["name"]} has no power, he is too young')


new_family = TheIncredibles(incredible_family)

