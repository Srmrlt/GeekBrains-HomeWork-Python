try:
    with open(r'files\file02.txt', 'r') as file_obj:
        lines = file_obj.readlines()
        for i, line in enumerate(lines):
            num_words = len(line.split())
            print(f'Number of words in line {i + 1}: {num_words}')
        print(f'Number of lines: {i+1}')
except IOError:
    print('Error while reading file')
