def div():
    arg_1 = float(input('Enter dividend: '))
    arg_2 = float(input('Enter divider: '))
    if arg_2 == 0:
        print('Division by zero!!!')
        return
    return arg_1 / arg_2


print(f'{div():.2f}')
