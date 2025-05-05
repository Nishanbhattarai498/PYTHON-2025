#method chaining = calling multiple methods on the same object in a single line of code
# This is a common pattern in Python and other programming languages that support object-oriented programming.


class Car:
    def turn_on(self):
        print("Car is turned on")
        return self
    
    def drive(self):

        print("Car is driving")
        return self
    
    def stop(self):

        print("Car is stopped")
        return self
    
    def turn_off(self):
        print("Car is turned off")
        return self
    

car=Car()
car.turn_on().drive().stop().turn_off()