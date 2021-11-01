# class Animal():
#     def __init__(self,name,legs):
#         self.name = name
#         self.legs = legs

#     def walk(self):
#         if self.legs:
#             print(f'the animal {self.name} walks on {self.legs} feet')
#         else:
#             print(f'{self.name} has no legs')


# class Dog(Animal):
#     def bark(self):
#         print('{} barked,WOOF!'.format(self.name))

# # animal1 = Animal('Frog')
# # animalw = Animal('Bird')
# dog = Dog('Sparky',4)

# # animal1.bark()
# # animalw.bark()
# dog.walk()
# dog.bark()
#--------------------------------------------------

'''We have a class called Door that has an attribute of is_opened declared when an instance is initiated.
We can create a class called BlockedDoor that inherits from the base class Door.
We just override the parent class's functions of open_door() and close_door()
 with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.

'''
import random
class Door:
    door_str = 'Door has been '
    def __init__(self,name=None):
        self.is_opened = random.choice([False,True])
        self.name =name or input('Where is the door located? '+ 'door')
    
    def open_door(self):
        self.is_opened = True
        print(self.door_str + 'opened')
    def close_door(self):
        self.is_opened = False
        print(self.door_str + 'closed')

class BlockedDoor(Door):
    def open_door(self):
        print('A blocked door cannot be opened or closed')
    def close_door(self):
        self.open_door()

door = Door()
blocked_door = BlockedDoor('Garage')
door.open_door()
blocked_door.open_door()
door.close_door()
blocked_door.close_door()
#----------------------------------------------------------
