# multi level inheritance = when a class is derived from a class which is also derived from another class 

# example of multi level inheritance

class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog=Dog()
print(dog.alive) # True
dog.eat() # This animal is eating
dog.sleep() # This animal is sleeping
dog.bark() # This dog is barking