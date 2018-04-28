# https://judge.softuni.bg/Contests/Practice/Index/152#12
import math

figure = input()
result = 'Invalid Result!'

if figure == 'square':
    a = float(input())
    result = str('%.3f' % (a * a))
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    result = str('%.3f' % (a * b))
elif figure == 'circle':
    r = float(input())
    result = str('%.3f' % (math.pi * r * r))
elif figure == 'triangle':
    a = float(input())
    h = float(input())
    result = str('%.3f' % (a * h / 2))

print(result)
