class Book:

    def __init__(self, title, author, year, quantity=1):
        self.title = title
        self.author = author
        self.year = year
        self.quantity = quantity

    def display_info(self):
        return "Print information about the book"

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}'

    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}'

class EBook(Book):
    def __init__(self, title, author, year, format_type, quantity=1):
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        return f'{super().display_info()} Additional information'

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}" \
               f" Format: {self.format_type}"


class Library:
    def __init__(self):
        self.books = []
        self.book_count = 0

    def add_book(self, book):
        self.books.append(book)
        self.book_count += 1

    def display_books(self):
        return "\n".join(str(book) for book in self.books)


class Customer:

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.quantity = 0
        print(f'{self.name} borrowed \'{book.title}\'.')

    def __str__(self):
        return f'{self.name} borrowed books:{self.borrowed_books}'


class LibraryManagementSystem:

    def __init__(self):
        self.library = Library()
        self.customers = []

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} registered in the system.")

    def display_customer_books(self, customer: Customer):
        borrowed_books_list = "\n".join(str(book) for book in customer.borrowed_books)
        print(f'Books borrowed by Alice:{borrowed_books_list}')

    def display_all_books(self):
        print(f'Books in the Library:\n{self.library.display_books()}')


book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2015, "PDF")
ebook2 = EBook("Dive into Python 3", "Mark Pilgrim", 2009, "EPUB")
customer1 = Customer("Alice")
customer2 = Customer("Bob")
library_system = LibraryManagementSystem()
library_system.register_customer(customer1)
library_system.register_customer(customer2)
library_system.library.add_book(book1)
library_system.library.add_book(book2)
library_system.library.add_book(ebook1)
library_system.library.add_book(ebook2)
customer1.borrow_book(book1)
customer1.borrow_book(ebook1)
customer2.borrow_book(book2)
library_system.display_customer_books(customer1)
library_system.display_all_books()