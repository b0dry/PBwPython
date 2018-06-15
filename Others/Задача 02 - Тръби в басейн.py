# https://judge.softuni.bg/Contests/Practice/Index/179#1

v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

result1 = p1 * h
result2 = p2 * h

if result1 + result2 < v:
    print('The pool is ' + str(int((result1 + result2) / v * 100)) + '% full. Pipe 1: ' +
          str(int(result1 / (result1 + result2) * 100)) + '%. Pipe 2: ' + str(int(result2 / (result1 + result2) * 100)) +
          '%.')
else:
    print('For ' +  + ' hours the pool overflows with ' +  + ' liters.')
