file = open("text.txt", "r")
# r - reading
# w - writing
# a - append
# r* - reading and writing

data = file.read()
data.replace(',', ' ')

data_into_list = data.split(",")

new_list = [["damn", 'shit']]
length = int(len(data_into_list)/4)
for i in range(length):
    if i >= 1:
        new_list.append(data_into_list[3 * i:7 * i])
    else:
        new_list.append(data_into_list[:3])
    i += 1

# print(data_into_list)

for i in new_list:
    print(i)
file.close()

print("damn idk what im doing")
