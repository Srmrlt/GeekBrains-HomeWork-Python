from math import factorial


def fact(x):
    for y in range(x + 1):
        val = factorial(y)
        yield f'{y}! = {val}'


for el in fact(5):
    print(el)
