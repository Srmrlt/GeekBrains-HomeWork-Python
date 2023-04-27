def div(dividend, divider):

    if divider == 0:
        return 'Division by zero!!!'
    return round(dividend / divider, 2)


try:
    arg_1 = float(input('Enter dividend: '))
    arg_2 = float(input('Enter divider: '))
    print(f'{div(arg_1, arg_2)}')
except ValueError:
    print('Value Error')
