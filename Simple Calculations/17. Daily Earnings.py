# https://judge.softuni.bg/Contests/Practice/Index/274#0

workdays = float(input())
daytips = float(input())
exchange_rate = float(input())

salary = workdays * daytips
annual_income = salary * 12 + salary * 2.5
neto_income = annual_income - annual_income * 25 / 100
result = neto_income / 365 * exchange_rate

print('%.2f' % result)
