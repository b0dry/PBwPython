# https://judge.softuni.bg/Contests/Practice/Index/1#0

x = float(input())
y = float(input())

result = -1

if x == y == 0:
    result = 0
elif x > 0 and y > 0:
    result = 1
elif x < 0 < y:
    result = 2
elif x < 0 and y < 0:
    result = 3
elif x == 0 and y != 0:
    result = 5
elif x != 0 and y == 0:
    result = 6
elif x > 0 > y:
    result = 4

print(result)
