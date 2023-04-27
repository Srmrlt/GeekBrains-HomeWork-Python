from sys import argv
script_name, hour, salary, benefit = argv
total = (int(hour) * int(salary)) + int(benefit)
print(total)
