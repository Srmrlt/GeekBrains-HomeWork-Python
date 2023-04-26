my_list = list(input('Enter list: '))
# my_list = ['1', '2', '3', '4', '5', '6', '7']
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print(' '.join(my_list))
