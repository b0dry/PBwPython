# https://judge.softuni.bg/Contests/Practice/Index/1#2

number = int(input())
for column in range(0, number):
    print(row * '.', end='')
    for row in range(0, number):
        print((abs(row - column) // 2) * '*', end='')
        print('.', end='')
        row += 1
    print('')
    column += 1
