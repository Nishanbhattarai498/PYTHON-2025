#abstract class : prevents instantiation of the class containing abstract methods

#abstract method : a method that is declared but contains no implementation



from abc import ABC, abstractmethod
# Abstract classs are classes that cannot be instantiated and are meant to be subclassed. They can contain abstract methods, which are methods that are declared but contain no implementation. Subclasses must implement these abstract methods.
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def go(self):
        print("Car is going")

    def stop(self):
        print("Car is stopping")

class Bike(Vehicle):
    def go(self):
        print("Bike is going")

    def stop(self):
        print("Bike is stopping")


# vehicle=Vehicle()
car=Car()
bike=Bike()

  # This will not do anything as Vehicle has no implementation for go()
car.go()  # Output: Car is going
bike.go()  # Output: Bike is going

car.stop()  # Output: Car is stopping
bike.stop()  # Output: Bike is stopping