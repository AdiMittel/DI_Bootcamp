class Farm():
    def __init__(self,name):
        self.name = name
        self.animals = {}

    def add_animal(self,animal,amount = 1):
        if animal in self.animals.keys():
            self.animals[animal] += amount
            print(self.animals)
            return self.animals
        else:
            self.animals[animal] = amount
            print(self.animals)

    def get_info(self):
        print(self.name + "Farm")
        for key, value in self.animals.items():
            print(f'{key} : {value} ')
        print('E-I-E-I-0!')


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()