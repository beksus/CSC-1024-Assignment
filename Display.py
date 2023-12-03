"""from Book import Book"""
import os

class Display:

    list = []
    def update_list(self,list):
        self.list=list

    # this function for printing content of object
    def display_books(self,list):
        print(f"{'Title': <20}{'Author': <20}{'Genre': <20}{'Publication Year': <20}{'Pages': <20}{'Publisher': <20}{'Language': <20}{'ISBN': <20}")

        for item in range(len(list)):
            #print(list[item].getter(0) + ' | ' + list[item].getter(1) + ' | ' + list[item].getter(2) + ' | ' + list[item].getter(3) + ' | '+list[item].getter(4) + ' | '+list[item].getter(5) + ' | '+list[item].getter(6) + ' | '+list[item].getter(7) )
            print(f"{list[item].getter(0): <20}{list[item].getter(1): <20}{list[item].getter(2): <20}{list[item].getter(3): <20}{list[item].getter(4): <20}{list[item].getter(5): <20}{list[item].getter(6): <20}{list[item].getter(7): <20}")
            print('\n')

    # i will finish it later
    def display_grid():
        pass
    
    def display_menu(self):
        print('Library Manager')
        print(" \n1 Add/Edit Books\n2 Delete Books\n3 Display Books\nChoose an option:")

    def display_options(self,index):
        if index is 1:
            print("1 Add Books\n2 Edit Books\nChoose an Option")
        elif index is 2:
            print('Enter ISBN/Title to delete')
        elif index is 3:
            self.display_books(self.list)
    
    def clearScreen(self):
        return os.system('cls' if os.name == 'nt' else 'clear')