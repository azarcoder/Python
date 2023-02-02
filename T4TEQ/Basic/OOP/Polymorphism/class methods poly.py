class Cat:
    def mood(self): 
       print("Grumpy") 
    def sound(self): 
       print("Meow") 
 
class Dog:
    def mood(self): 
       print("Happy") 
    def sound(self): 
       print("Woof") 
 
hello_kitty = Cat()
hello_puppy = Dog()
 
for pet in (hello_kitty, hello_puppy):
    pet.mood()
    pet.sound()
