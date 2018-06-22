# https://judge.softuni.bg/Contests/Practice/Index/179#2

budget = float(input())
season = input('')

if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        print('Camp - ' + '{0:.2f}'.format(0.30 * budget))
    else:
        print('Hotel - ' + '{0:.2f}'.format(0.70 * budget))
elif budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        print('Camp - ' + '{0:.2f}'.format(0.40 * budget))
    else:
        print('Hotel - ' + '{0:.2f}'.format(0.80 * budget))
else:
    print('Somewhere in Europe')
    print('Hotel - ' + '{0:.2f}'.format(0.90 * budget))
