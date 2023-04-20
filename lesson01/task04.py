val = input(f'Enter positive integer: ')
'''
i = 0
val_max = 0
while i < len(val):
    if val_max < int(val[i]):
        val_max = int(val[i])
    i = i + 1
print(f'Largest number: {val_max}')
'''
val_max = max(val)
print(f'Largest number: {val_max}')
