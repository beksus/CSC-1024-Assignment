from Book import Book
from Display import Display

"""isbn = "9780747532686"
author = 'JK Rowling'
title = "Harry Potter and the Philosopher's Stone"
publisher = "Bloomsbury"
genre = "Fantasy"
date_published = '1997'
date_purchased = '15-03-2020'
status = 'to-read'
list = [isbn,author,title,publisher,genre, date_published, date_purchased,status]"""


#object book has a values above
#book = Book(isbn,author,title,publisher,genre, date_published, date_purchased,status)

# you can call and get all values
#print(book.__str__())

# you can call and get value with integer from 1 to 8
#print(book.getter(5))

list=[]
display = Display()

while True:
    display.clearScreen()

    display.update_list(list)
    display.display_menu()
    choice = str(input(""))
    display.clearScreen()
    if choice == '1':
        while True:
            display.display_options(1)
            choice = str(input('Choose an Option: '))
            if choice == '1':
                break
            else:
                print('Invalid Choice')
        display.clearScreen()


    else:
        print('Invalid Choise')