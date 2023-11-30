from Book import Book
from Display import Display


file = open("book_list.txt", "r")
# r - reading
# w - writing
# a - append
# r* - reading and writing

data = file.readlines()
data
new_list = []




# getting the values from text file
for line in data:
    line_strip = line.strip()
    line_split = line_strip.split(',')
    new_list.append(line_split)

list = []



for i in range(len(new_list)):
     list.append(Book(new_list[i][0] ,new_list[i][1],new_list[i][2],new_list[i][3],new_list[i][4],new_list[i][5],new_list[i][6],new_list[i][7], ))

"""for item in range(len(new_list)):
        new_list[item] = Book(new_list[item])
         """


for item in new_list:
    print(item)

# printing details
"""for item in range(len(list)):
    
    print(list[item].getter(0) + ' | ' + list[item].getter(1) + ' | ' + list[item].getter(2) + ' | ' + list[item].getter(3) + ' | '+list[item].getter(4) + ' | '+list[item].getter(5) + ' | '+list[item].getter(6) + ' | '+list[item].getter(7) )
    print('\n')"""


disp = Display()

disp.display_books(list)


file.close()

