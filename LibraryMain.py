# notification this is main filed of Main file 
# notice it is not finished still raw i will finish it later

from Book import Book
from Display import Display
from Delete import Delete

# notification: this is still raw and look immature so i will finish it later
# you made a change here

# this list is for storing the book objects
list=[]
# this variable to initialize the Display class
display = Display()
delete = Delete()

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
                # code
                break
            elif choice == '2':
                # code
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
            choice = str(input('Choose an Option: '))
            if choice == '1':
                # code
                break
            elif choice != '1':
                print("deleted")
                #delete.delete_book(list,str(choice))
            else:
                display.clearScreen()
                print('Invalid Choice')
    elif choice == '3':
        while True:
            display.display_options(3)
            choice = str(input('Choose an Option: '))
            if choice == '1':
                # code
                break
            elif choice == '2':
                # code
                break
            elif choice == '3':
                break
            else:
                display.clearScreen()
                print('Invalid Choice')
        display.clearScreen()
    else:
        print('Invalid Choise')