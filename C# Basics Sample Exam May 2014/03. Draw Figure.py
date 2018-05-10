# https://judge.softuni.bg/Contests/Practice/Index/1#2

number = int(input())

for column in range(number // 2 + 1):
    d = column * '.'
    s = (number - 2 * column) * '*'
    print(f'{d}{s}{d}')

for c in range(number // 2 - 1, -1, -1):
    d = c * '.'
    s = (number - 2 * c) * '*'
    print(f'{d}{s}{d}')
