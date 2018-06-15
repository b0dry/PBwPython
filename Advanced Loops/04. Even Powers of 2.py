# https://judge.softuni.bg/Contests/Practice/Index/156#3

n = int(input())

for b in range(n+1):
    if b % 2 == 0:
        print(pow(2, b))
