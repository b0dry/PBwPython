# https://judge.softuni.bg/Contests/Practice/Index/179#3

n = int(input())
ranges = [0, 0, 0]
for i in range (0, n):
    tmp = int(input())
    if tmp % 2 == 0:
        ranges[0] += 1
    if tmp % 3 == 0:
        ranges[1] += 1
    if tmp % 4 == 0:
        ranges[2] += 1

for r in ranges:
    tmp = r / n * 100
    print(f'%.2f' % tmp + '%')
