def my_sum():
    total = 0
    run = True
    while run:
        num_string = input('Enter array of numbers: ')
        if num_string == '#':
            break
        num_list = num_string.split()
        for num in num_list:
            if num == '#':
                run = False
                break
            total += int(num)
        print(total)


my_sum()
