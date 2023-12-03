from Book import Book
from Display import Display

isbn = "9780747532686"
author = 'JK Rowling'
title = "Harry Potter and the Philosopher's Stone"
publisher = "Bloomsbury"
genre = "Fantasy"
date_published = '1997'
date_purchased = '15-03-2020'
status = 'to-read'
list = [isbn,author,title,publisher,genre, date_published, date_purchased,status]


#object book has a values above
book = Book(list)

# you can call and get all values
#print(book.__str__())

# you can call and get value with integer from 1 to 8
print(book.getter(5))

display = Display()

while True:

    choice = input("")