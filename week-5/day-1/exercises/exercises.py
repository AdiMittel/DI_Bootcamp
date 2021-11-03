# 1
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat_list):
    cat = sorted(cat_list, key=lambda cat: cat.age)[-1]
    return cat


data_list = [('rex', 21), ('snow', 65), ('mitzi', 34)]

cats = [Cat(*data) for data in data_list]

oldest = oldest_cat(cats)
# print(f'Oldest cat is {oldest.name} its {oldest.age} years old!')

# --------------------------------------
# 2


# class Dog():
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f'{self.name} goes WOOF!')

#     def jump(self):
#         x = self.height * 2
#         print(f'{self.name} jump {x} cm high!')


# davids_dog = Dog('Rex', 50)
# print(davids_dog.name, davids_dog.height)
# davids_dog.jump()

# sarahs_dog = Dog('Teacup', 20)
# print(sarahs_dog.name, sarahs_dog.height)
# sarahs_dog.jump()

# if sarahs_dog.height > davids_dog.height:
#     print(f'{sarahs_dog} is heigher than David\'s dog')
# else:
#     print(f'{davids_dog.name} is heigher than sarahs dog')

# -----------------------------------------------------
# 3
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold",
                "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# ----------------------------------------
# 4
class Zoo():
    
    def __init__(self,zoo_name):
        self.animals = []
        self.animals_dict = {}
        self.name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            return self.animals.append(new_animal)
            

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            index = self.animals.index(animal_sold)
            self.animals.pop(index)
    
    def sort_animals(self):
        temp_l = sorted(self.animals)
        i = 1
        while len(temp_l) > 0:
            n_list = [temp_l[0]]
            temp_l.pop(0)
            try:
                while temp_l[0][0] == n_list[0][0]:
                    n_list.append(temp_l[0])
                    temp_l.pop(0)
                self.animals_dict[i] = n_list
                i+=1
            except:
                self.animals_dict[i] = n_list
        return self.animals_dict
        
    def get_groups(self):
        for group in self.animals_dict.values():
            print(*group)




ramat_gan_safari = Zoo('Ramat gan safari')
ramat_gan_safari.add_animal('Tiger')
ramat_gan_safari.add_animal('Cow')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Chicken')
ramat_gan_safari.add_animal('Buffalo')
ramat_gan_safari.add_animal('Parrot')

# zoo.sell_animal('Cow')
# zoo.get_animals()
print(ramat_gan_safari.sort_animals())
ramat_gan_safari.get_groups()