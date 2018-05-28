# https://judge.softuni.bg/Contests/Practice/Index/179#4

n = int(input())

for row in range(0, n - 2):
    if row % 2 == 0:
        print((n - 2) * '*' + '\\ /' + (n - 2) * '*')
    else:
        print((n - 2) * '-' + '\\ /' + (n - 2) * '-')

print((n - 1) * ' ' + '@')

for row in range(0, n - 2):
    if row % 2 == 0:
        print((n - 2) * '*' + '/ \\' + (n - 2) * '*')
    else:
        print((n - 2) * '-' + '/ \\' + (n - 2) * '-')