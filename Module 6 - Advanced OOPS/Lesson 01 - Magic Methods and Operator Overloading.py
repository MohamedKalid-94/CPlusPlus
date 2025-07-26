class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __str__(self):
        return f"Book with {self.pages} pages"

book1 = Book(150)
book2 = Book(200)

print(book1 + book2)  # Output: 350
print(book1)          # Output: Book with 150 pages