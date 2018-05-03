# https://judge.softuni.bg/Contests/Practice/Index/911#1

total_dough_weight = int(input())
dough_per_bread = int(input())
dough_per_sweet = int(dough_per_bread * 0.80)
bread_price = float(input())
sweets_price = float(bread_price * 1.25)
bread_amount = int(input())
sweets_amount = int(input())

income = 0
dough = 0

day_income = bread_amount * bread_price
night_income = sweets_amount * sweets_price
day_dough = dough_per_bread * bread_amount
night_dough = dough_per_sweet * sweets_amount

expenses = ((total_dough_weight + day_dough)/1000) * 4
income = day_income + night_income - expenses
dough = day_dough + night_dough

print(f'Pure income: {income} lv.')
print(f'Dough used: {dough} g.')
