result = int(input(f'Enter your current result: '))
ambition = int(input(f'Enter your ambitions: '))
day = 1
while result < ambition:
    result = result * 1.1
    day = day + 1
    print(f'Day {day}: {result:.2f}')
print(f'Day you will reach your ambitions: {day}')