# https://judge.softuni.bg/Contests/Practice/Index/169#0

w = float(input())
h = float(input())

rows = int(w * 100 / 120)
height = int(((h * 100) - 100) / 70)

print(rows * height - 3)
