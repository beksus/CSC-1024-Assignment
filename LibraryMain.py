# notification this is main filed of Main file 
# notice it is not finished still raw i will finish it later
from Book import Book
from Display import Display
from Delete import Delete
from AddEdit import AddEdit
from Delete import Delete

# notification: this is still raw and look immature so i will finish it later
# you made a change here

# this list is for storing the book objects
list = []
new_list = []
# this variable to initialize the Display class
display = Display()
delete = Delete()
add_new_books = AddEdit()
file = open("book_list.txt", "r")
data = file.readlines()
for line in data:
    line_strip = line.strip()
    line_split = line_strip.split(',')
    new_list.append(line_split)
    
for i in range(len(new_list)):
     list.append(Book(new_list[i][0] ,new_list[i][1],new_list[i][2],new_list[i][3],new_list[i][4],new_list[i][5],new_list[i][6],new_list[i][7] ))


# main flow for program wich is not finished
while True:

    display.clearScreen()

    # this calling of funciton of saving the list inside of display to manage it easier
    display.update_list(list)

    # this is displaying the main menu options
    display.display_grid()
    display.display_menu()

    # this is input for execution
    choice = str(input(""))

    # after input the previously prints should be deleted from screen
    display.clearScreen()
    display.display_grid()
    # statements for options
    if choice == '1':
        while True:
            display.display_options(1)
            choice = str(input('Choose an Option: '))
            if choice == '1':
                list = add_new_books.add_book(list)
                input('Press enter to exit: ')
                break
            elif choice == '2':
                list = add_new_books.edit_book(list)
                input('Press enter to exit: ')
                break
            elif choice == '3':
                break
            else:
                display.clearScreen()
                print('Invalid Choice')
        display.clearScreen()

    elif choice == '2':
        while True:
            display.display_options(2)
            choice = str(input(' [1] Delete\n [2] Exit\nChoose an Option: '))
            if choice == '1':
                if delete.delete_book(list, str(input("Enter "))) == 1:
                    print("Book Deleted Successfully")
                    input("Press enter to exit: ")
                else:
                    print("Book not found")
                break
            elif choice == '2':
                break
                #delete.delete_book(list,str(choice))
            else:
                display.clearScreen()
                print('Invalid Choice')
    elif choice == '3':
        while True:
            display.display_options(3)
            choice = str(input('Choose an Option: '))
            if choice == '1':
                display.display_books(list)
                input('Press enter to exit: ')
            elif choice == '2':
                display.display_search(list, str(input('Enter Books name: ')))
                input('Press enter to exit: ')
                display.clearScreen()
                break
                
            elif choice == '3':
                break
            else:
                display.clearScreen()
                print('Invalid Choice')
        display.clearScreen()
    else:
        print('Invalid Choise')

        