#✅ Inheritance Example:
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()  # Output: Bark

#✅ Composition Example:
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car *has-a* Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

c = Car()
c.drive()