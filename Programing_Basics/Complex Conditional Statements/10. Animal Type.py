# https://judge.softuni.bg/Contests/Practice/Index/153#9

animal = input()

if animal in ('dog'):
    print('mammal')
elif animal in ('crocodile', 'tortoise', 'snake'):
    print('reptile')
else:
    print('unknown')
