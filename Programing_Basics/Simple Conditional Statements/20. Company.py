# https://judge.softuni.bg/Contests/Practice/Index/274

"""
Вход
Входът се чете от конзолата и съдържа точно 3 реда:
 На първия ред са необходимите часовете – цяло число в интервала [0 ... 200 000]
 На втория ред са дните, с които фирмата разполага – цяло число в интервала [0 ... 20 000]
 На третия ред е броят на служителите, работещи извънредно – цяло число в интервала [0 ... 200]
Изход
Да се отпечата на конзолата един ред:
 Ако времето е достатъчно:
o “Yes!{оставащите часове} hours left.”
 Ако времето НЕ Е достатъчно:
o “Not enough time!{недостигащите часове} hours needed.“

"""
import math

# Console input
needed_hours = int(input())
days_available = int(input())
extra_workers = int(input())

# calculations
extra_hours = extra_workers * 2 * days_available
days_available *= 0.9
hours_available = days_available * 8
total_hours = math.floor(extra_hours + hours_available)
calculated_hours = total_hours - needed_hours

# Logic and Console output
if calculated_hours >= 0:
    print(f'Yes!{calculated_hours} hours left.')
else:
    print(f'Not enough time!{abs(calculated_hours)} hours needed.')
