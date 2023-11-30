class Book:
    def __init__(self, title, author, genre, publication_year, pages, publisher, language, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.pages = pages
        self.publisher = publisher
        self.language = language
        self.isbn = isbn

    def getter(self, index):
        return [self.title, self.author, self.genre, self.publication_year, self.pages, self.publisher, self.language, self.isbn][index]


class Display:

    def display_books(self, list):
        # Display books in the list
        print(f"{'Title': <20}{'Author': <20}{'Genre': <20}{'Publication Year': <20}{'Pages': <20}{'Publisher': <20}{'Language': <20}{'ISBN': <20}")
        for book in list:
            print(f"{book.getter(0): <20}{book.getter(1): <20}{book.getter(2): <20}{book.getter(3): <20}{book.getter(4): <20}{book.getter(5): <20}{book.getter(6): <20}{book.getter(7): <20}")

    def display_grid():
        # Display a grid layout
        pass

# Testing
book1 = Book("The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, 234, "Little, Brown, and Company", "English", "978-0316769488")
book2 = Book("1984", "George Orwell", "Dystopian", 1949, 328, "Secker & Warburg", "English", "978-0451524935")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 267, "Charles Scribner's Sons", "English", "978-0743273565")
book_list = [book1, book2, book3]
display = Display()
display.display_books(book_list)