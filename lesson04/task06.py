from itertools import count
from itertools import cycle


def int_gen(start, stop):
    for el in count(start):
        if el > stop:
            break
        print(el)


def list_repeater():
    fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango', 'grape', 'kiwi', 'watermelon', 'pear']
    for el in cycle(fruits):
        if input('q for exit: ') == 'q':
            break
        print(el)


int_gen(3, 6)
list_repeater()
