# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class StreetCat(Cat):
#     def sing(self,sounds):
#         return f'{sounds}'

# cat1 = Bengal('mitzi',3)
# cat2 = Chartreux('fluffy',5)
# cat3 = StreetCat('ted',10)
# cats_list = [cat1,cat2,cat3]
# sounds_list = ['meow','grrr','prrr']

# for i in range(len(cats_list)):
#     print(cats_list[i].sing(sounds_list[i]))


# my_pets = Pets(cats_list)
# my_pets.walk()
#---------------------------------------------------------
class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        self.speed = self.age/self.weight*10
        return self.speed
    
    def fight(self,other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            winner = self.name
            print(f'{winner} is the winner')
        else:
            winner = other_dog.name
            print(f'{winner} is the winner')
 
#  The winner should be the dog with the higher run_speed x weight.
dog1 = Dog('diggo',10,10)
dog2 = Dog('doggo',6,4)
dog3 = Dog('spark',5,12)
dog1.fight(dog2)
print(dog3.bark())