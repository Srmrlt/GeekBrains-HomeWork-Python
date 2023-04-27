def my_func(x, y):
    n_1 = x ** y
    n_2 = 1
    for i in range(abs(y)):
        n_2 *= x
    if y < 0:
        n_2 = 1 / n_2
    return n_1, n_2


print(my_func(2, -3))
