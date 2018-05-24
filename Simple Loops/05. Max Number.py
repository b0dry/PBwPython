# https://judge.softuni.bg/Contests/Practice/Index/154#4

amount = int(input())

result = int(input())

for i in range(1, amount):
    tmp = int(input())
    if tmp > result:
        result = tmp

print(result)
