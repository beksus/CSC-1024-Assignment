from Book import Book
from Display import Display
from Validator import Validator
class AddEdit:

    """def __init__(self, book):
         self.book = book
         #add a new book to the database
         if(not self.book.is_valid()):
              raise ValueError("Book is not valid")
         self.display = Display()
         def add_new_book(self):
              print "Adding New Book"
              title = raw_input('Enter Title of the Book : ')
              author = raw_input('Enter Author Name : ')
              price = float(raw_input('Enter Price of the Book : '))
              publisher = raw_input('Enter Publishers name : ')
              year = int(raw_input('Enter Year Published : '))
              genre = raw_input('Enter Genre : ')
              pages = int(raw_input('Number of Pages in this book : '))
              ISBN = input('Enter ISBN number (if any) : ')
              description = raw_input('Enter Description about the book : ')
              imagePath = raw_input('Enter Image Path for the book cover : ')
              book = Book(title=title,author=author,price=price,publisher=publisher,year=year,genre=genre)"""
    def add_book(list):
        disp = Display()
        
        while True: 
                isbn = input("Enter the ISBN of the book: ")
                length = len(isbn)
                if length >= 10 and  length <= 13 and isbn.isnumeric():
                    break
                else:
                    disp.clearScreen()
                    print("Please Enter Valid Numbers for ISBN between 10 and 13 digit numbers")
            
        disp.clearScreen()

        while True:

                name = input("Enter the Name of the Author: ")
                surename = input("Enter the Surname of the Author: ")
                # the author's name should contain only alphabets so .isaplpha is a validator for valid name
                if name.isalpha and name.isalpha:
                    name.casefold
                    surename.casefold
                    author = f"{name.title()} {surename.title()}"
                    break
                
                disp.clearScreen()
                print("Please Enter Valid Name and Surname for Book Author!")

        disp.clearScreen()

        while True:

                title = input("Enter the title of the book: ")
                # the title's name should contain only alphanumerical and not just numbers
                # for that .isalpha finds that name contains number or not 
                # for detecting digit .isdigit should give false for valid name 
                if title.isalnum:
                    break

                disp.clearScreen()
                print("Please Enter Valid Title for Book Author!")
            
        disp.clearScreen()

        while True:

                publisher = input("Enter the publisher of the book: ")
                # statement to find out is the publisher has name as alphanumeric and not as numeric and not alphabetical
                if publisher.isalnum:
                    break

                disp.clearScreen()
                print("Please Enter Valid Name of Publisher!")

        disp.clearScreen()

        while True:

                genre = input("Enter the genre of the book: ")
                # the genre can contain only alphabetical letters
                if genre.isalnum:
                    break
                disp.clearScreen()
                print("Please Enter Genre of the Book!")

        disp.clearScreen()
        while True:

                date_published = input("Enter the date published of the book: ")
                # statement for finding that year published is consist of 4 digit number and is it a digit
                if len(date_published) == 4 and date_published.isdigit:
                    break
                print("Please enter a valid Year Published!")
            
        disp.clearScreen()
            
        while True:
                
                day_purchased = input("Enter the day purchased of the book: ")
                month_purchased = input("Enter the month purchased of the book: ")
                year_purchased = input("Enter the year purchased of the book: ")
                # statement for finding that day, month, and year is digit
                # also year should be containing 4 digit number
                if day_purchased.isdigit and month_purchased.isdigit and year_purchased.isdigit and len(year_purchased) == 4 and year_purchased >= date_published:
                    # dd-mm-yyyy is format for date purchased
                    date_purchased = f'{day_purchased}-{month_purchased}-{year_purchased}'
                    break
                print("Please enter a valid Date Purchased!")

        disp.clearScreen()

        while True:
                print(' [1] read\n [2] to-read\n [3] reading')
                status_input = input("Enter the status of the book in range of 1-3: ")
                status_type = ['read', 'to-read','reading']

                # statement to check whether the entered string contains only alphabets or not and is it in range pf 1 to 3
                if status_input.isdigit() and int(status_input) < 4 and int(status_input) > 0:
                    status = status_type[int(status_input)-1]
                    break
                print("Please enter a valid book status!")
            
        disp.clearScreen()
            
        # creating book object and adding to existing list of objects
        list.append(Book(isbn, author, title, publisher, genre, date_published, date_purchased, status))
        return list
        
            

    def edit_book(list):

        index = {
        1: 'id',
        2: 'title',
        3: 'author',
        4: 'publisher',
        5: 'genre',
        6: 'date_published',
        7: 'date_purchased',
        8: 'status'
        }

        disp = Display()
        # default values
        book_index = 0
        value = None
        boole = True
        
        #disp.clearScreen()
        while boole:
            index = int(input("Enter the isbn of the book which you want to update: "))
            for i in range(len(list)):
                if list[i].getter(0) == str(index):
                    boole = False
                    break
                elif list[i].getter(0) != str(index):
                    book_index += 1

            if boole == True:
                disp.clearScreen()
                print("Please enter existing book!")
        disp.clearScreen()
        # default value
        choice = 8
        while True:
            choice = input(" [1] ISBN\n [2] Title\n [3] Author's Name\n [4] Publisher\n [5] Genre\n [6] Date Published\n [7] Date Purchased\n [8] status\n [9] Exit \nChoose an option: ")
            try:
                if choice.isdigit and int(choice) < 9 and int(choice) > 0:
                    disp.clearScreen()
                    choice = choice
                    #value = input(f"Enter value to change {index[int(choice)]} : ")
                    #list[book_index].update(choice, value)
                    break
                elif int(choice) == 9 and choice.isdigit:
                    return list
                else:
                    disp.clearScreen()
                    print('Please input valid numbers in range of 1 to 8')
            except:
                disp.clearScreen()
                print('Please input valid numbers in range of 1 to 8')

        
        if int(choice) == 1:
            while True: 
                value = input(" [1] Exit\nEnter the ISBN of the book: ")
                length = len(value)
                if length >= 10 and  length <= 13 and value.isnumeric():
                    break
                elif value.isdigit and int(value) == 1:
                     return list
                else:
                    disp.clearScreen()
                    print("Please Enter Valid Numbers for ISBN between 10 and 13 digit numbers")

        elif int(choice) == 2:
            while True:
                print(" [1] Exit\n")
                name = input("Enter the Name of the Author: ")
                surename = input("Enter the Surname of the Author: ")
                # the author's name should contain only alphabets so .isaplpha is a validator for valid name
                try:
                    if name.isalpha and name.isalpha:
                        name.casefold
                        surename.casefold
                        value = f"{name.title()} {surename.title()}"
                        break
                    elif int(name) == 1:
                        return list
                    else:
                        disp.clearScreen()
                        print('Please input valid numbers in range of 1 to 8')
                except:
                    disp.clearScreen()
                    print("Please Enter Valid Name and Surname for Book Author!")

        elif int(choice) == 3:
            while True:

                value = input(" [1] Exit\nEnter the title of the book: ")
                # the title's name should contain only alphanumerical and not just numbers
                # for that .isalpha finds that name contains number or not 
                # for detecting digit .isdigit should give false for valid name
                try:
                    if value.isalnum:
                        break
                    elif int(value) == 1 and value.isdigit:
                         return list
                    else:
                        disp.clearScreen()
                        print("Please Enter Valid Title for Book Author!")
                except:
                    disp.clearScreen()
                    print("Please Enter Valid Title for Book Author!")

        elif int(choice) == 4:
            while True:
                value = input(" [1] Exit\nEnter the publisher of the book: ")
                try:
                    
                    # statement to find out is the publisher has name as alphanumeric and not as numeric and not alphabetical
                    if value.isalnum:
                        break
                    elif int(value) == 1 and value.isdigit:
                        return list
                    else:
                        disp.clearScreen()
                        print("Please Enter Valid Name of Publisher!")
                except:
                    disp.clearScreen()
                    print("Please Enter Valid Name of Publisher!")

        elif int(choice) == 5:
            while True:

                value = input(" [1] Exit\nEnter the genre of the book: ")
                try:
                    # the genre can contain only alphabetical letters
                    if value.isalnum:
                        break
                    elif int(value) == 1:
                        return list
                    else:
                        disp.clearScreen()
                        print("Please Enter Genre of the Book!")
                         
                except:
                    disp.clearScreen()
                    print("Please Enter Genre of the Book!")

        elif int(choice) == 6:
            while True:

                value = input(" [1] Exit\nEnter the date published of the book: ")
                # statement for finding that year published is consist of 4 digit number and is it a digit
                try:
                    if len(value) == 4 and value.isdigit:
                        break
                    elif int(value) == 1:
                         return list
                    else: 
                        disp.clearScreen()
                        print("Please enter a valid Year Published!")
                except:
                    disp.clearScreen()
                    print("Please enter a valid Year Published!")
            
        elif int(choice) == 7:
            while True:
                
                day_purchased = input(" [1] Exit\nEnter the day purchased of the book: ")

                if int(day_purchased) == 1:
                    return list
                
                month_purchased = input("Enter the month purchased of the book: ")
                year_purchased = input("Enter the year purchased of the book: ")
                # statement for finding that day, month, and year is digit
                # also year should be containing 4 digit number
                if day_purchased.isdigit and month_purchased.isdigit and year_purchased.isdigit and len(year_purchased) == 4:
                    # dd-mm-yyyy is format for date purchased
                    value = f'{day_purchased}-{month_purchased}-{year_purchased}'
                    break
                print("Please enter a valid Date Purchased!")

        elif int(choice) == 8:
            while True:
                print(' [1] read\n [2] to-read\n [3] reading\n [4] Exit')
                status_input = input("Enter the status of the book in range of 1-3: ")

                status_type = ['read', 'to-read','reading']

                # statement to check whether the entered string contains only alphabets or not and is it in range pf 1 to 3
                if status_input.isdigit() and int(status_input) < 4 and int(status_input) > 0:
                    value = status_type[int(status_input)-1]
                    list[book_index].update_status(value)
                    print(list[book_index].getter(7))
                    break
                elif status_input == 4 and status_input.isdigit():
                    return list
                
                print("Please enter a valid book status!")
        
        
        list[book_index].update(int(choice)-1, value)

        return list
        
                                            
          



