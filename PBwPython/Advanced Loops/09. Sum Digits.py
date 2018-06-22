# https://judge.softuni.bg/Contests/Practice/Index/156#8

n = int(input())
result = 0
while n > 0:
    result = result + n % 10
    n = n // 10

print(result)
