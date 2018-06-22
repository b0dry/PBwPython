# https://judge.softuni.bg/Contests/Practice/Index/274#2

month = input()
nights = int(input())
apartment_result = 0
studio_result = 0

if month in ('May', 'October'):
    apartment_result = nights * 65
    studio_result = nights * 50
    if 14 >= nights > 7:
        studio_result = studio_result * 0.95
    elif nights > 14:
        studio_result = studio_result * 0.70
elif month in ('June', 'September'):
    apartment_result = nights * 68.70
    studio_result = nights * 75.20
    if nights > 14:
        studio_result = studio_result * 0.80
else:
    apartment_result = nights * 77
    studio_result = nights * 76

if nights > 14:
    apartment_result = apartment_result * 0.90


print('Apartment: {0:.2f} lv.'.format(apartment_result))
print('Studio: {0:.2f} lv.'.format(studio_result))
