# Overriding Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
d = Dog()
a.speak()  # Output: Animal speaks
d.speak()  # Output: Dog barks

# Overloading workaround using default args
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2))        # Output: 2
print(calc.add(2, 3))     # Output: 5
print(calc.add(2, 3, 4))  # Output: 9
