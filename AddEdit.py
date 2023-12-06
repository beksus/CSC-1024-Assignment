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
                # the author's name should contain only alphabets so .isaplpha is a validator for valid name
                if name.isalpha and name.isalpha:
                    name.casefold
                    surename.casefold
                    author = f"{name.title()} {surename.title()}"
                    break
                
                print("Please Enter Valid Name and Surname for Book Author!")

            self.disp.clearScreen()

            while True:

                title = input("Enter the title of the book: ")
                # the title's name should contain only alphanumerical and not just numbers
                # for that .isalpha finds that name contains number or not 
                # for detecting digit .isdigit should give false for valid name 
                if title.isalnum and title.isalpha == False and title.isdigit == False:
                    break

                print("Please Enter Valid Name and Surname for Book Author!")
            
            self.disp.clearScreen()

            while True:

                publisher = input("Enter the title of the book: ")
                # statement to find out is the publisher has name as alphanumeric and not as numeric and not alphabetical
                if publisher.isalnum and publisher.isalpha == False and publisher.isdigit == False:
                    break

                print("Please Enter Valid Name of Publisher!")

            self.disp.clearScreen()
            while True:

                genre = input("Enter the title of the book: ")
                # the genre can contain only alphabetical letters
                if genre.isalpha and genre.isdigit == False:
                    break
                
                print("Please Enter Genre of the Book!")

            self.disp.clearScreen()
            while True:

                year_published = input("Enter the date published of the book: ")
                # statement for finding that year published is consist of 4 digit number and is it a digit
                if len(year_published) == 4 and year_published.isdigit:
                    break
                print("Please enter a valid Year Published!")
            
            self.disp.clearScreen()
            
            while True:
                
                day_purchased = input("Enter the day purchased of the book: ")
                month_purchased = input("Enter the month purchased of the book: ")
                year_purchased = input("Enter the year purchased of the book: ")
                # statement for finding that day, month, and year is digit
                # also year should be containing 4 digit number
                if day_purchased.isdigit and month_purchased.isdigit and year_purchased.isdigit and len(year_purchased) == 4:
                    # dd-mm-yyyy is format for date purchased
                    date_purchased = f'{day_purchased}-{month_purchased}-{year_purchased}'
                    break
                print("Please enter a valid Date Purchased!")

            self.disp.clearScreen

            while True:
                print('[1] read\n [2] to-read\n[reading]')
                status_input = input("Enter the status of the book in range of 1-3: ")
                status_type = ['read', 'to-read','reading']

                # statement to check whether the entered string contains only alphabets or not and is it in range pf 1 to 3
                if status.isdigit() and status <4 and status>0:
                    status = status_type[status_input-1]
                    break
                print("Please enter a valid book status!")
            
            self.disp.clearScreen
            
            # creating book object and adding to existing list of objects
            list.append(Book(isbn, author, publisher , genre , year_published, date_purchased, status))





