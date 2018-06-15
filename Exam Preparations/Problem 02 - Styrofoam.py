# https://judge.softuni.bg/Contests/Practice/Index/501#1

import math

budget = float(input())
house_area = float(input())
windows = int(input())
square_meters_per_package = float(input())
price = float(input())

cost_styrofoam = 0
left = 0
needs = 0

cost_styrofoam = math.ceil(((house_area - windows * 2.4) * 1.1) / square_meters_per_package) * price

if budget >= cost_styrofoam:
    print('Spent: {0:.2f}'.format(cost_styrofoam))
    print('Left: {0:.2f}'.format(budget - cost_styrofoam))
else:
    print('Need more: {0:.2f}'.format(cost_styrofoam - budget))
