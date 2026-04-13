class Animal():
    def __init__(self, name, weight, breed, legs):
        self.name = name
        self.weight = weight
        self.breed = breed
        self.__legs = legs
        
    def rename(self, new_name):
        self.name = new_name
        print(f'Now the animals name is {self.name}.')

    @property
    def legs(self):
        return self.__legs
    
    @legs.setter
    def legs(self, new):
        if new < 2 or new > 40:
            print(f"{new} Beine sind nicht zulässig!")
        else:
            self.__legs = new
            print(f"Die neue Anzahl der Beine von {self.name}: {self.__legs}.")


class Dog(Animal):
    def __init__(self, name, weight, breed, legs, give_paw):
        super().__init__(name, weight, breed, legs)
        self.give_paw = give_paw

    def speak(self):
        print(f'{self.name} barks')


    # def plus_weight(self):
    #     self.weight += 1
    #     print(f'The new weight of {self.name} -> {self.weight}')


class Cat(Animal):
    def __init__(self, name, weight, breed, legs, is_climbing):
        super().__init__(name, weight, breed, legs)
        self.is_climbing = is_climbing

    def speak(self):
        print(f'{self.name} says "meow!"')

kostya = Cat('Kostya', 5, 'Siamese', 4, False)
sharik = Dog('Sharik', 10, 'Bulldog', 4, True)

kostya.speak()
sharik.speak()



# print(kostya.legs)
# kostya.legs = -1000
# kostya.legs = 40
# kostya.legs = 41


pets = [Dog('Jerryk', 10, 'Bulldog', 4, True), Dog('Taisy', 10, 'Bulldog', 4, True), Cat('Murzik', 5, 'Siamese', 4, False), Cat('Vasya', 5, 'Siamese', 4, False)]

for pet in pets:
    pet.speak()