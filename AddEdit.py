from Book import Book
from Display import Display
class AddEdit:
    disp = Display()
    def add_book(self, list):

        while True:
            while True: 
                isbn = input("Enter the ISBN of the book: ")
                length = len(isbn)
                if length >= 10 and  length <= 13 and isbn.isnumeric():
                    break
                else:
                    print("Please Enter Valid Numbers for ISBN between 10 and 13 digit numbers")
            self.disp.clearScreen()
            while True:

                name = input("Enter the Name of the Author: ")
                surename = input("Enter the Surname of the Author: ")
                
                if name.isalpha and name.isalpha:
                    name.casefold
                    surename.casefold
                    author = f"{name.title()} {surename.title()}"
                    break
                
                print("Please Enter Valid Name and Surname for Book Author!")

            self.disp.clearScreen()

            while True:

                title = input("Enter the title of the book: ")
                if title.isalnum and title.isalpha == False and title.isdigit == False:
                    break

                print("Please Enter Valid Name and Surname for Book Author!")
            
            self.disp.clearScreen()

            while True:

                publisher = input("Enter the title of the book: ")
                if publisher.isalnum and publisher.isalpha == False and publisher.isdigit == False:
                    break

                print("Please Enter Valid Name of Publisher!")

            self.disp.clearScreen()
            while True:

                genre = input("Enter the title of the book: ")

                if genre.isalpha:
                    break

            year_published = input("Enter the title of the book: ")

            date_purchased = input("Enter the title of the book: ")

            status = input("Enter the title of the book: ")

            name = f'{name} {surename}'

            list.append(Book(isbn, author, publisher , genre , year_published, date_purchased, status))





