income = int(input(f'Income for this month: '))
expenses = int(input(f'Expenses this month: '))
revenue = income - expenses
if income < expenses:
    print(f'Loss this month: {revenue}')
else:
    print(f'Profit this month: {revenue}')
    employee_num = int(input(f'Enter number of employees: '))
    revenue_employee = revenue / employee_num
    print(f'Profit per employee this month: {revenue_employee}')
