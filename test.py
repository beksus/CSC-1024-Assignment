from Book import Book


file = open("book_list.txt", "r")
# r - reading
# w - writing
# a - append
# r* - reading and writing

data = file.readlines()
data
new_list = []


for line in data:
    line_strip = line.strip()
    line_split = line_strip.split(',')
    new_list.append(line_split)

list = []

for i in range(len(new_list)):
     list.append(Book(new_list[i]))

"""for item in range(len(new_list)):
        new_list[item] = Book(new_list[item])
         """


for item in new_list:
    print(item)

# printing details
for item in list:
    
    print(str(item.getter(1)) + ' | ' + str(item.getter(2)) + ' | ' + item.getter(3) + ' | ' + item.getter(4) + ' | '+item.getter(5) + ' | '+item.getter(6) + ' | '+item.getter(7) + ' | '+item.getter(8) )
    print('\n')


file.close()

