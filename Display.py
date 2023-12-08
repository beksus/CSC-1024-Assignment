# notification: this is main field of Display

import os

class Display:

    list = []
    def update_list(self,list):
        self.list=list

    # this function for printing content of object
    def display_books(self,list):
        # printing the heading of contents
        print(f"{'ISBN':<18}{'Author': <20}{'Title': <35}{'Publisher': <13}{'Genre': <10}{'Date': <7}{'Purchased': <10}{'Status': <5}")

        # printing the contents
        for item in range(len(list)):
            #print(list[item].getter(0) + ' | ' + list[item].getter(1) + ' | ' + list[item].getter(2) + ' | ' + list[item].getter(3) + ' | '+list[item].getter(4) + ' | '+list[item].getter(5) + ' | '+list[item].getter(6) + ' | '+list[item].getter(7) )
            print(f"{list[item].getter(0)} | {list[item].getter(1)} | {list[item].getter(2)} | {list[item].getter(3)} | {list[item].getter(4)} | {list[item].getter(5)} | {list[item].getter(6)} | {list[item].getter(7)}")
            print('\n')

    def display_search(self, list, key):
        index = 0
        print(f"{'ISBN':<18}{'Author': <20}{'Title': <35}{'Publisher': <13}{'Genre': <10}{'Date': <7}{'Purchased': <10}{'Status': <5}")
        for i in range(len(list)):
            for j in range(8):
                if key == list[i].getter(j):
                    print(f"{list[i].getter(0)} | {list[i].getter(1)} | {list[i].getter(2)} | {list[i].getter(3)} | {list[i].getter(4)} | {list[i].getter(5)} | {list[i].getter(6)} | {list[i].getter(7)}")


        #print(f"{'ISBN':<18}{'Author': <20}{'Title': <35}{'Publisher': <13}{'Genre': <10}{'Date': <7}{'Purchased': <10}{'Status': <5}")
        #print(f"{list[index].getter(0)} | {list[index].getter(1)} | {list[index].getter(2)} | {list[index].getter(3)} | {list[index].getter(4)} | {list[index].getter(5)} | {list[index].getter(6)} | {list[index].getter(7)}")

    # i will finish it later
    def display_grid(self):
        print("         .-----.           .---.       \n     .---|-----|   .-.     | A |  .---.")
        print("     |***|hello|---|_|--.__| S |__|^^^|\n .---|   |world|===| |__|KH| C |  |   |")
        print(" |%%%|C# |     |IVN| |  |  | I |--|BRN|\n |BEK|   |     |===|_|  |**| I |  |   |")
        print(" |   |   |     |   | |__|  |~~~|--|^^^|\n |   |   |#####|===|_|  |NV|   |  |   |")
        print(" ^---^---^-----^---^-^--^--^---^--^---^")
    
    # prints the main menu options
    def display_menu(self):
        print('Library Manager')
        print(" \n1 Add/Edit Books\n2 Delete Books\n3 Display Books\nChoose an option:")

    # prints the option for options for chosen option
    def display_options(self,index):
        if index == 1:
            print(" [1] Add Books\n [2] Edit Books\n [3]Exit")
        elif index == 2:
            print('Enter ISBN or Title to delete\n [1] Exit')
        elif index == 3:
            print(" [1] Display All Books\n [2] Display Search\n [3]Exit")
            #self.display_books(self.list)
        

    # be carefull with this code
    # it can delete the whole text output after run so it will be cleaner to read the display
    # if you don't understand then paste code to ai and ask it or search it in internet of youtube with titile of "python clear text output"
    def clearScreen(self):
        return os.system('cls' if os.name == 'nt' else 'clear')