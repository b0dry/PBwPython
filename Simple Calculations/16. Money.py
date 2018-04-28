# Условието на задачата е грешно спрямо проверките тук: https://judge.softuni.bg/Contests/Practice/Index/233#0

btcs = float(input())
uahs = float(input())
commission = float(input())

USD = 1.76
UAH = 0.15 * USD
EUR = 1.95
BTC = 1168
BGN = 1

btcs_result = btcs * BTC
uahs_result = uahs * UAH

print('%.2f' % (((btcs_result + uahs_result) - (btcs_result + uahs_result) * commission / 100) / EUR))

