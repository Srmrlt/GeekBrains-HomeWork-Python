from sys import argv
from itertools import count
from itertools import cycle

script_name = argv
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango', 'grape', 'kiwi', 'watermelon', 'pear']
for el in cycle(fruits):
    if input('q for exit: ') == 'q':
        break
    else:
        print(el)
