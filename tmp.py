sleeve = int(input())
front = int(input())
material = input()
tie = input()

size = (sleeve * 2 + front * 2) * 1.1 / 100
price = 0
sewing = 10

if material == "Linen":
    price = size * 15 + sewing
elif material == "Cotton":
    price = size * 12 + sewing
elif material == "Denim":
    price = size * 20 + sewing
elif material == "Twill":
    price = size * 16 + sewing
elif material == "Flannel":
    price = size * 11 + sewing

if tie == "Yes":
    price *= 1.2

print(f'The price of the shirt is: {price:.2f}lv.')
