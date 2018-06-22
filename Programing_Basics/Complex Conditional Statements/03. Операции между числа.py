# https://judge.softuni.bg/Contests/Practice/Index/181#2

n1 = int(input())
n2 = int(input())
operator = input()
parity = ''

if operator == '*':
    if (n1 * n2) % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    print(f'{n1} {operator} {n2} = {n1 * n2} - {parity}')
elif operator == '/':
    if n2 == 0:
        print('Cannot divide ' + str(n1) + ' by zero')
    else:
        print(f'{n1} / {n2} = ' + '{0:.2f}'.format(n1/n2))
elif operator == '+':
    if (n1 + n2) % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    print(f'{n1} {operator} {n2} = {n1 + n2} - {parity}')
elif operator == '-':
    if (n1 - n2) % 2 == 0:
        parity = 'even'
    else:
        parity = 'odd'
    print(f'{n1} {operator} {n2} = {n1 - n2} - {parity}')
elif operator == '%':
    if n2 == 0:
        print('Cannot divide ' + str(n1) + ' by zero')
    else:
        print(f'{n1} {operator} {n2} = ' + str(n1 % n2))
