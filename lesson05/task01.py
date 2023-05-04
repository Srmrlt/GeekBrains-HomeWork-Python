out_file = open(r'files\file01.txt', 'w')
while True:
    my_str = input('Enter line (empty line for exit): ')
    if not my_str:
        break
    out_file.write(f'{my_str}\n')
out_file.close()
