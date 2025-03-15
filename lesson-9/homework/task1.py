# Step 1: Define Custom Exceptions
class BookNotFoundException(Exception):
    """Raised when trying to borrow a book that does not exist."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when trying to borrow a book that is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member tries to borrow more books than allowed."""
    pass


# Step 2: Define Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Initially, the book is available.

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


# Step 3: Define Member Class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # Stores borrowed books (max: 3 books).

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} has already borrowed 3 books!")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book.title}' is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name} (Borrowed: {', '.join(borrowed_titles) if borrowed_titles else 'None'})"


# Step 4: Define Library Class
class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books (title -> Book object)
        self.members = {}  # Dictionary to store members (name -> Member object)

    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        print(f"Added book: '{title}' by {author}")

    def add_member(self, name):
        self.members[name] = Member(name)
        print(f"Added member: {name}")

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library!")
        if member_name not in self.members:
            print(f"Member '{member_name}' not found. Please register first.")
            return

        member = self.members[member_name]
        book = self.books[book_title]

        try:
            member.borrow_book(book)
        except (BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")

    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            print(f"Member '{member_name}' not found.")
            return
        if book_title not in self.books:
            print(f"Book '{book_title}' not found in the library.")
            return

        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members.values():
            print(member)


# Step 5: Test Scenarios
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    # Add members
    library.add_member("Alice")
    library.add_member("Bob")

    # Display books and members
    library.display_books()
    library.display_members()

    # Borrow books
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "To Kill a Mockingbird")

    # Try borrowing a 4th book (should raise an exception)
    library.borrow_book("Alice", "Moby Dick")  # This book is not in the library

    # Try borrowing an already borrowed book
    library.borrow_book("Bob", "1984")

    # Returning books
    library.return_book("Alice", "1984")
    library.borrow_book("Bob", "1984")  # Now Bob can borrow it

    # Final state
    library.display_books()
    library.display_members()
