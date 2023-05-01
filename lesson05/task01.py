from sys import stdin

out_file = open(r'files\file01.txt', 'w')
while True:
    my_str = stdin.readline()
    if my_str == '\n':
        break
    out_file.write(f'{my_str}')
out_file.close()
