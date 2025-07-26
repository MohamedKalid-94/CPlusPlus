class Dog:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object correctly
my_dog = Dog(name="Buddy", brand="Golden Retriever")

# Output
print(my_dog.bark())
