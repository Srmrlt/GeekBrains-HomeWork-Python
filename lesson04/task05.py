from functools import reduce


def my_func(pr_el, el):
    return pr_el * el


my_list = [el for el in range(100, 1000+1) if el % 2 == 0]
multiplication = reduce(my_func, my_list)
print(multiplication)
