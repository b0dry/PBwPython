# https://judge.softuni.bg/Contests/Practice/Index/155#4

n = int(input())

for i in range (1, n + 1):
    if i == 1 or i == n:
        print('+ ' + '- ' * (n - 2) + '+')
    else:
        print('| ' + '- ' * (n - 2) + '|')
