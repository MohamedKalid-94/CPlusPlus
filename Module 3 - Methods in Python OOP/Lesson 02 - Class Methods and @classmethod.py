class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

p1 = Person("Alice")
p2 = Person("Bob")
print("Person count:", Person.get_count())  # Output: Person count: 2
