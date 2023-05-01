from math import factorial


def fact(x):
    for y in range(x):
        val = factorial(y + 1)
        yield val


for el in fact(3):
    print(f'factorial: {el}')
