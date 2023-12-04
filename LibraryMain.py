from Book import Book
from Display import Display

# notification: this is still raw and look immature so i will finish it later


# this list is for storing the book objects
list=[]
# this variable to initialize the Display class
display = Display()


# main flow for program wich is not finished
while True:

    #display.clearScreen()

    # this calling of funciton of saving the list inside of display to manage it easier
    display.update_list(list)

    # this is displaying the main menu options
    display.display_menu()

    # this is input for execution
    choice = str(input(""))

    # after input the previously prints should be deleted from screen
    display.clearScreen()

    # statements for options
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