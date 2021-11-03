class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = {}

    def add_animal(self,animal,amount = 1):
        self.animals[animal] = amount
        return self.animals

    def get_info(self):
        for key, value in self.animals.items():
            if key == key



macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())