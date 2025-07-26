class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

    def details(self):
        return f"'{self.title}' by {self.author}"

# Creating instances
my_book = Book(title="1984", author="George Orwell")
author_book = Book("Untitled")

# Output
print(my_book.details())       # '1984' by George Orwell
print(author_book.details())   # 'Untitled' by Unknown
