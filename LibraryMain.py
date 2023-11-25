<<<<<<< Updated upstream
x = True

while x:
    print("OPTION: \n1 import books\n2 delete/edit\n3 display\n4 exit")
    y = input("Enter option:")

    if(y == '1'):
        print('success')
    elif(y == '2'):
        print('success')
    elif(y == '3'):
        print('success')
    elif(y == '4'):
        print('ByeBye')
        x = False
    else:
        print('failure!!! try again')
print('template')

=======
from Book import Book

isbn = "9780747532686"
author = 'JK Rowling'
title = "Harry Potter and the Philosopher's Stone"
publisher = "Bloomsbury"
genre = "Fantasy"
date_published = '1997'
date_purchased = '15-03-2020'
type = 'to-read'

#object book has a values above
book = Book(isbn, author, title, publisher, genre,date_published,date_purchased,type)

# you can call and get all values
print(book.__str__())

# you can call and get value with integer from 1 to 8
print(book.getter(1))
>>>>>>> Stashed changes
