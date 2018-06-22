# https://judge.softuni.bg/Contests/Practice/Index/155#6

n = int(input())

for row in range(1, n + 2):
    print(' ' * (n + 1 - row), end='')
    print('*' * (row - 1) + ' | ' + '*' * (row - 1))
