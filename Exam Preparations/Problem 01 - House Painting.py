# https://judge.softuni.bg/Contests/Practice/Index/499#0

x = float(input())
y = float(input())
h = float(input())

green_drain = ((x * x * 2 - 2.4) + (x * y * 2 - 2 * 2.25)) / 3.4
red_drain = (x * y * 2 + x * h) / 4.3

print('{0:.2f}'.format(green_drain))
print('{0:.2f}'.format(red_drain))
