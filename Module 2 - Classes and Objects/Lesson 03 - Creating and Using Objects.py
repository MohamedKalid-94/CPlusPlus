# Defining the class
class Car:
    def __init__(self, brand, model, year):
        # Instance variables
        self.brand = brand
        self.model = model
        self.year = year

    def description(self):
        # Method to return a formatted description
        return f"{self.year} {self.brand} {self.model}"

# Creating objects (instances of the class)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)

# Using the objects and calling their methods
print(car1.description())  # Output: 2020 Toyota Corolla
print(car2.description())  # Output: 2021 Honda Civic
