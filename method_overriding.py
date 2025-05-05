class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def eat(self):
        print("Dog is eating")

dog = Dog()
dog.eat()  # Output: Animal is eating