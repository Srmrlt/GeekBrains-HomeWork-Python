from sys import argv

try:
    hour, salary, benefit = map(int, argv[1:])
    total = (hour * salary + benefit)
    print(total)
except ValueError:
    print('Incorrect values')
