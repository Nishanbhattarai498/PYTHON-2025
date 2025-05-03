from car import Car
# Compare this snippet from car.py:
car_1 = Car("Toyota", "Camry", 2020, "Blue")
car_2 = Car("Honda", "Civic", 2019, "Red")
car_3 = Car("Ford", "Mustang", 2021, "Black")
car_4 = Car("Chevrolet", "Malibu", 2018, "White")
print(car_1.make, car_1.model, car_1.year, car_1.color)
print(car_2.make, car_2.model, car_2.year, car_2.color)
print(car_3.make, car_3.model, car_3.year, car_3.color)
print(car_4.make, car_4.model, car_4.year, car_4.color)

car_1.drive()
car_1.stop()
