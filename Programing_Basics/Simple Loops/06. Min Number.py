# https://judge.softuni.bg/Contests/Practice/Index/154#5

# https://judge.softuni.bg/Contests/Practice/Index/154#4
import sys

amount = int(input())

result = sys.maxsize

for i in range(0, amount):
    tmp = int(input())
    if tmp < result:
        result = tmp

print(result)
