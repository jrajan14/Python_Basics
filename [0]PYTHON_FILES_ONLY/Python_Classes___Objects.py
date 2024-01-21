# Python Basics
# Classes and Objects in Python

# Class declaration 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    
    def drive(self, distance):
        self.mileage += distance
        print(f"The {self.year} {self.make} {self.model} has now driven {self.mileage} miles.")
    
    def honk(self):
        print("Honk honk!")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2023)

# Using methods on the objects
car1.drive(100)
car2.drive(75)

car1.honk()
