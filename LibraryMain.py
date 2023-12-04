from Book import Book
from Display import Display





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