from exercise import Dog
import random
class PetDog(Dog):
    
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.is_trained = trained

    def traine(self):
        print(self.bark())
        self.is_trained = True

    def play(self,*args):
        for arg in args:
            print(f'{arg} are playing')

    def do_a_trick(self):
        bag_of_tricks = [' Do a backflip',' Roll over',' Play dead',' Shake my hand']
        trick = random.choice(bag_of_tricks)
        if self.is_trained:
            print(self.name + trick)

dog = PetDog('spike',5,6,True)

# dog.play('a','s','r','k')

dog.do_a_trick()