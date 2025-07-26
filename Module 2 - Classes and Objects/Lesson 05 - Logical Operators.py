# Logical Operators: and, or, not

# Define some variables
x = 10
y = 5
z = 15

# Using AND operator
print("AND Operator:")
print(x > y and z > x)   # True and True => True
print(x > y and z < x)   # True and False => False

# Using OR operator
print("\nOR Operator:")
print(x > y or z < x)    # True or False => True
print(x < y or z < x)    # False or False => False

# Using NOT operator
print("\nNOT Operator:")
print(not(x > y))        # not True => False
print(not(x < y))        # not False => True
