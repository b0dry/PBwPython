import math

n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    left_sum += int(input())

for i in range(0, n):
    right_sum += int(input())

if left_sum == right_sum:
    print("Yes, sum=%d" % left_sum)
else:
    diff = math.fabs(left_sum - right_sum)
    print("No, diff=%d" % diff)
