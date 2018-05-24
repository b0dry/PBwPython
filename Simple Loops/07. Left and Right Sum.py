# https://judge.softuni.bg/Contests/Practice/Index/154#6

amount = int(input())

left = 0
right = 0

for a in range(0, amount):
    left += int(input())

for b in range(0, amount):
    right += int(input())

if left == right:
    print('Yes, sum = ' + str(left))
else:
    print('No, diff = ' + str(abs(left - right)))
