from abc import ABC, abstractmethod
class Animals(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Description:
    def animal_description(self):
        pass
class Cow(Animals,Description):
    def make_sound(self):
        print("Mooooo ! \n")
    def animal_description(self):
        print("Cows is a herbivores animals as they eat grass and vegetables\n")
class Cat(Animals,Description):
    def make_sound(self):
        print("Meow Meow !\n")
    def animal_description(self):
        print("Cats are a nice animal you can tame it, they eat vegans and meat\n")
class Dog(Animals,Description):
    def make_sound(self):
        print("Whoof ! Whof !\n")
    def animal_description(self):
        print("Dogs are a nice animal you can tame it, they eat meat. they are loyal too\n")

dog1 = Dog()
cow1 = Cow()
cat1 = Cat()
dog1.make_sound()
dog1.animal_description()
cat1.make_sound()
cat1.animal_description()
cow1.make_sound()
cow1.animal_description()