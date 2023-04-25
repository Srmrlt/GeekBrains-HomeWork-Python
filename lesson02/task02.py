my_list = list(input('Enter list: '))
# my_list = [1, 2, 3, 4, 5, 6, 7]
i = 1
while i < len(my_list):
    my_list[i-1], my_list[i] = my_list[i], my_list[i-1]
    i += 2
print(my_list)
