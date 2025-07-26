class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins can't fly")

b = Bird()
p = Penguin()

b.fly()  # Bird can fly
p.fly()  # Penguins can't fly
