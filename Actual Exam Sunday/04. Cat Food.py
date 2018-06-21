# https://judge.softuni.bg/Contests/Compete/Index/1045#3

cat_amount = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
food = 0.00

for cat in range(cat_amount):
    temp = float(input())
    if temp < 200:
        group_1 += 1
    elif 200 <= temp < 300:
        group_2 += 1
    elif 300 <= temp:
        group_3 += 1
    food += temp

price = food * 0.01245

print(f'Group 1: {group_1} cats.')
print(f'Group 2: {group_2} cats.')
print(f'Group 3: {group_3} cats.')
print(f'Price for food per day: {price:.2f} lv. ')
