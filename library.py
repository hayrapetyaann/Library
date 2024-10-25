class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Available: {self.available}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
        else:
            print(f"{self.name} did not borrow {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"{book.title} not found in the library.")

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def search_book_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def search_book_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn == isbn]

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, user, book):
        user.borrow_book(book)

    def return_book(self, user, book):
        user.return_book(book)

    def add_user(self, user):
        self.users.append(user)

library = Library()
book1 = Book("Python", "Jane", "1234567890")
book2 = Book("Effective C++", "Doe", "0987654321")

user1 = User("1", "Name")
user2 = User("2", "Anun")

library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)

library.display_books()
library.borrow_book(user1, book1)
library.display_books()
library.return_book(user1, book1)
library.display_books()
