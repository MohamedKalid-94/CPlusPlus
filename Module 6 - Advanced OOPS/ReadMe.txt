Understanding Magic Methods and Operator Overloading
Objective:
Learn how special/magic methods allow us to customize class behavior, especially for operator overloading (e.g., +, ==, len()).
Definition:
Magic methods (also called dunder methods) are special methods with double underscores before and after their names (e.g., __init__, __str__, __add__).
Operator Overloading is customizing how operators work with user-defined classes.

🔥 Common Magic Methods:
Method	        Purpose
__init__	    Constructor
__str__	        String representation
__add__	        Overload + operator
__len__	        Overload len() function
__eq__	        Overload == operator
__lt__	        Overload < operator

Creating Custom Iterators and Generators
🎯 Objective:
Learn how to build your own iterable objects using __iter__() and __next__() or using generator functions with yield.
🔍 Definition:
An iterator is an object that implements __iter__() and __next__().
A generator is a simpler way to create iterators using yield.

Understanding Composition vs Inheritance
🎯 Objective:
Understand the difference between reusing functionality through inheritance and building complex classes using composition.
🔍 Definitions:
Inheritance: A class (child) inherits from another class (parent). Use when there's an "is-a" relationship.
Composition: One class contains objects of other classes. Use when there's a "has-a" relationship.