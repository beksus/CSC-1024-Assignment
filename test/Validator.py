from Display import Display
class Validator:
    
    def __init__(self):
        pass

    def check_value_input(choice):
        disp = Display
        if choice == 1:
            while True: 
                value = input("Enter the ISBN of the book: ")
                length = len(value)
                if length >= 10 and  length <= 13 and value.isnumeric():
                    return value
                else:
                    disp.clearScreen()
                    print("Please Enter Valid Numbers for ISBN between 10 and 13 digit numbers")

        elif choice == 2:
            while True:

                name = input("Enter the Name of the Author: ")
                surename = input("Enter the Surname of the Author: ")
                # the author's name should contain only alphabets so .isaplpha is a validator for valid name
                if name.isalpha and name.isalpha:
                    name.casefold
                    surename.casefold
                    value = f"{name.title()} {surename.title()}"
                    return value
                
                disp.clearScreen()
                print("Please Enter Valid Name and Surname for Book Author!")

        elif choice == 3:
            while True:

                value = input("Enter the title of the book: ")
                # the title's name should contain only alphanumerical and not just numbers
                # for that .isalpha finds that name contains number or not 
                # for detecting digit .isdigit should give false for valid name 
                if value.isalnum:
                    return value

                disp.clearScreen()
                print("Please Enter Valid Title for Book Author!")

        elif choice == 4:
            while True:

                value = input("Enter the publisher of the book: ")
                # statement to find out is the publisher has name as alphanumeric and not as numeric and not alphabetical
                if value.isalnum:
                    return value

                disp.clearScreen()
                print("Please Enter Valid Name of Publisher!")

        elif choice == 5:
            while True:

                value = input("Enter the genre of the book: ")
                # the genre can contain only alphabetical letters
                if value.isalnum:
                    return value
                disp.clearScreen()
                print("Please Enter Genre of the Book!")

        elif choice == 6:
            while True:

                value = input("Enter the date published of the book: ")
                # statement for finding that year published is consist of 4 digit number and is it a digit
                if len(value) == 4 and value.isdigit:
                    return value
                disp.clearScreen()
                print("Please enter a valid Year Published!")
            
        elif choice == 7:
            while True:
                
                day_purchased = input("Enter the day purchased of the book: ")
                month_purchased = input("Enter the month purchased of the book: ")
                year_purchased = input("Enter the year purchased of the book: ")
                # statement for finding that day, month, and year is digit
                # also year should be containing 4 digit number
                if day_purchased.isdigit and month_purchased.isdigit and year_purchased.isdigit and len(year_purchased) == 4:
                    # dd-mm-yyyy is format for date purchased
                    value = f'{day_purchased}-{month_purchased}-{year_purchased}'
                    return value
                disp.clearScreen()
                print("Please enter a valid Date Purchased!")

        elif choice == 8:
            while True:
                print(' [1] read\n [2] to-read\n [3] reading')
                status_input = input("Enter the status of the book in range of 1-3: ")
                status_type = ['read', 'to-read','reading']

                # statement to check whether the entered string contains only alphabets or not and is it in range pf 1 to 3
                if status_input.isdigit() and int(status_input) < 4 and int(status_input) > 0:
                    value = status_type[int(status_input)-1]
                    return value
                disp.clearScreen()
                print("Please enter a valid book status!")

        return -1
