# notification: this is main test field of code 
# if you want to understand how it work please read comments below

from Book import Book
from Display import Display
from AddEdit import AddEdit


file = open("book_list.txt", "r")
# r - reading
# w - writing
# a - append
# r* - reading and writing

data = file.readlines()


# this list is to save text content as a string format in 2d array
new_list = []

add_new_books = AddEdit


# getting the values from text file
for line in data:
    line_strip = line.strip()
    line_split = line_strip.split(',')
    new_list.append(line_split)


#this list for carrying object 
list = []


# creating object from list taking the values and saving it to the object as Book
for i in range(len(new_list)):
     list.append(Book(new_list[i][0] ,new_list[i][1],new_list[i][2],new_list[i][3],new_list[i][4],new_list[i][5],new_list[i][6],new_list[i][7] ))

"""for item in range(len(new_list)):
        new_list[item] = Book(new_list[item])
         """

# this is how the new list look like as it is saved string in 2d array
for item in new_list:
    print(item)

# printing details
"""for item in range(len(list)):
    
    print(list[item].getter(0) + ' | ' + list[item].getter(1) + ' | ' + list[item].getter(2) + ' | ' + list[item].getter(3) + ' | '+list[item].getter(4) + ' | '+list[item].getter(5) + ' | '+list[item].getter(6) + ' | '+list[item].getter(7) )
    print('\n')"""

# displayer
disp = Display()

disp.display_books(list)
list = add_new_books.edit_book(list)
print("\n\n")
disp.display_books(list)



file.close()

