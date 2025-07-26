class Father:
    def skills(self):
        print("Fishing and carpentry")

class Mother:
    def skills(self):
        print("Cooking and painting")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()
