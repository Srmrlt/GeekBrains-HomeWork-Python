my_dict = {'Name': None, 'Price': None, 'Quantity': None, 'Unit': None}
my_list = []

while True:
    for el in my_dict.keys():
        ent = input(f'Enter {el}: ')
        my_dict.update({el: ent})
    my_list.append((len(my_list) + 1, my_dict.copy()))

    if input('Print end for stop: ') == 'end':
        break
print(my_list)

for key in my_dict.keys():
    tm_list = []
    for el in my_list:
        val = el[1].get(key)
        tm_list.append(val)
    my_dict.update({key: tm_list})
print(my_dict)
