my_dict = {'Name': None, 'Price': None, 'Quantity': None, 'Unit': None}
ind = 1
my_list = []

while True:
    for el in my_dict.keys():
        ent = input(f'Enter {el}: ')
        my_dict.update({el: ent})
    my_list.append((ind, my_dict.copy()))
    ind += 1

    if input('Print end for stop: ') == 'end':
        break

for key in my_dict.keys():
    tm_list = []
    for el in my_list:
        val = el[1].get(key)
        tm_list.append(val)
    my_dict.update({key: tm_list})
print(my_dict)
