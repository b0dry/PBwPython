# https://judge.softuni.bg/Contests/Practice/Index/1#1

# Input data
n1 = int(input())
n2 = int(input())
n3 = int(input())
length = int(input())

# Variables
result = ''

# Calculations
if length == 1:
    result = n1
elif length == 2:
    result = n2
elif length == 3:
    result = n3
else:
    for n in range(0, length - 3):
        result = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = result
        n += 1
# Display result
print(result)
