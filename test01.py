# notification: this is test fielf of Book and Display


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
        print(f"{'Title': <15}{'Author': <15}{'Genre': <15}{'Publication Year': <15}{'Pages': <15}{'Publisher': <15}{'Language': <15}{'ISBN': <15}")
        for book in list:
            print(f"{book.getter(0): <17}|{book.getter(1): <17}|{book.getter(2): <17}|{book.getter(3): <17}|{book.getter(4): <17}|{book.getter(5): <17}|{book.getter(6): <17}|{book.getter(7): <17}")

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
de = str(input("enter book to delete: "))
try:
    for i in book_list:
        if i.getter(7) == de:
            book_list.remove(i)
            print("deleted")
        elif i.getter(0) == de:
            book_list.remove(i)
            print("deleted")
        elif i.getter(1) == de:
            book_list.remove(i)
            print("deleted")
except Exception:
    print("this book doesn't exist")

""" if book_list[i].getter(7) is de:
        book_list.remove(i)
        print("deleted", book_list[i])
    elif book_list[i].getter(0) is de:
        book_list.remove(i)
        print("deleted", book_list[i])
    elif book_list[i].getter(1) is de:
        book_list.remove(i)
        print("deleted", book_list[i])"""



display.display_books(book_list)
