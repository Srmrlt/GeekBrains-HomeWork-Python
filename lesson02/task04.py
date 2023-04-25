text = input('enter several words: ')
# text = 'раз два три 01234567890123'
words = text.split()
for ind, el in enumerate(words, 1):
    if len(el) > 10:
        el = el[:10]
    print(f'{ind}: {el}')
