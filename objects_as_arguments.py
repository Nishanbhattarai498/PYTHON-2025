class Car:

    color =None

class Motorcycle:
    color = None


def change_color(car, color):
    car.color = color


bike_1 = Motorcycle()
bike_2 = Motorcycle()

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "green")
change_color(bike_1, "yellow")
change_color(bike_2, "black")


print(car_1.color)  # Output: None
print(car_2.color)  # Output: None
print(car_3.color)  # Output: None
print(bike_1.color)  # Output: None
print(bike_2.color)  # Output: None