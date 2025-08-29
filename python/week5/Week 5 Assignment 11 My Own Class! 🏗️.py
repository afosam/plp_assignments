# 📚 Simple Book Class

class Book:
    # Constructor to set up the book
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # Method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."
    
    # Method to check if the book is long or short
    def is_long(self):
        return "This is a long book." if self.pages > 300 else "This is a short book."

# ✅ Create objects (each book is unique)
book1 = Book("Python Basics", "Alice Walker", 120)
book2 = Book("The Art of AI", "John Smith", 450)

# 🖨️ Display info
print(book1.describe())
print(book1.is_long())
print(book2.describe())
print(book2.is_long())