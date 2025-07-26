class Person:
    def __init__(self, name, age):
        self.name = name              # public variable
        self._email = "test@mail.com" # protected variable
        self.__age = age              # private variable

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age

# Creating an object
p = Person("John", 25)

print(p.name)        # Public access - allowed
print(p._email)      # Protected access - allowed but not recommended
# print(p.__age)     # ❌ Private access - not allowed
print(p.get_age())   # ✅ Access via getter method
