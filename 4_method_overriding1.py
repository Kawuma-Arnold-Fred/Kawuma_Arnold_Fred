class Animal:
    def make_sound(self):
        print('Make animal sound')
        
class Cow(Animal):
    def make_sound(self):
        print('Moooo')
        
class Sheep(Animal):
    def make_sound(self):
        print('Baaaa')

def animal_sound(animal):
    animal.make_sound()
    
Molly = Cow()
Barry = Sheep()

Molly.make_sound()
Barry.make_sound()        
