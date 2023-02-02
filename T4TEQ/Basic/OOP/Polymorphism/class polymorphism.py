class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
 
    def make_sound(self):
        print("Meow")
 
 
class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def info(self):
        print(f"I am a Cow. My name is {self.name}. I am {self.age} years old.")
 
    def make_sound(self):
        print("Moo")
cat1 = Cat("Kitty", 2.5)
cow1 = Cow("Fluffy", 4)
 
for animal in (cat1, cow1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
