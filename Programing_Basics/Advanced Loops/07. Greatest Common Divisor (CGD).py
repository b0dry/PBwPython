# https://judge.softuni.bg/Contests/Practice/Index/156#6

a = int(input())
b = int(input())

while not b == 0:
    t = b
    b = a % b
    a = t

print(a)
