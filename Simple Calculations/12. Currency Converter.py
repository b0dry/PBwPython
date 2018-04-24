amount = float(input())
fr = input()
to = input()
USD = 1.79549
EUR = 1.95583
GBP = 2.53405
BGN = 1

GBP = {'GBP', 2.53405}

if fr == 'USD':
    if to == 'EUR':
        amount = amount * USD / EUR
    elif to == 'GBP':
        amount = amount * USD / GBP
    elif to == 'BGN':
        amount = amount * USD / BGN
    elif to == 'USD':
        amount = amount * USD / USD

if fr == 'EUR':
    if to == 'EUR':
        amount = amount * EUR / EUR
    elif to == 'GBP':
        amount = amount * EUR / GBP
    elif to == 'BGN':
        amount = amount * EUR / BGN
    elif to == 'USD':
        amount = amount * EUR / USD

if fr == 'GBP':
    if to == 'EUR':
        amount = amount * GBP / EUR
    elif to == 'GBP':
        amount = amount * GBP / GBP
    elif to == 'BGN':
        amount = amount * GBP / BGN
    elif to == 'USD':
        amount = amount * GBP / USD

if fr == 'BGN':
    if to == 'EUR':
        amount = amount * BGN / EUR
    elif to == 'GBP':
        amount = amount * BGN / GBP
    elif to == 'BGN':
        amount = amount * BGN / BGN
    elif to == 'USD':
        amount = amount * BGN / USD

print(str(round(amount, 2)) + ' ' + to)
