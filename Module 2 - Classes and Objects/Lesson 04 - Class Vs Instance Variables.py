# Class Definition
class Student:
    # Class variable - shared by all instances
    school_name = "Green Valley High School"

    # Constructor - initializes instance variables
    def __init__(self, name, grade):
        # Instance variables - unique to each object
        self.name = name
        self.grade = grade

    # Instance method - can access instance and class variables
    def show_details(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}")

# Creating objects (instances) of the class
student1 = Student("Alice", "10th")
student2 = Student("Bob", "9th")

# Accessing instance and class variables using method
student1.show_details()
print("---")
student2.show_details()
