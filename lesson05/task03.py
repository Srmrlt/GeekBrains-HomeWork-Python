from statistics import mean

try:
    with open(r'files/file03.txt', 'r') as file:
        employee_list = file.readlines()
        salary = [int(line.split()[1]) for line in employee_list]
        salary_avg = mean(salary)
        print(f'Average salary: {salary_avg}')
        low_salary_list = [line for line in employee_list if int(line.split()[1]) < salary_avg]
        for i, val in enumerate(low_salary_list):
            print(f'{i + 1}: {val[:-1]}')
except IOError:
    print('Error while reading file')


