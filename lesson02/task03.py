months = ['', 'winter', 'winter', 'autumn', 'autumn', 'autumn', 'summer',
          'summer', 'summer', 'spring', 'spring', 'spring', 'winter']

seasons = {12: 'winter', 1: 'winter', 2: 'winter',
           3: 'autumn', 4: 'autumn', 5: 'autumn',
           6: 'summer', 7: 'summer', 8: 'summer',
           9: 'spring', 10: 'spring', 11: 'spring'}

month_number = int(input('Enter month number: '))
print(months[month_number])
print(seasons.get(month_number))
