val = input(f'Enter number n: ')
val_n = int(val)
val_nn = int(f'{val}{val}')
val_nnn = int(f'{val}{val}{val}')
result = val_n + val_nn + val_nnn
print(f'Result of n + nn + nnn: {result}')
