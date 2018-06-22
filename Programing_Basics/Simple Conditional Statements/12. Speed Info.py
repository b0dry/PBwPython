# https://judge.softuni.bg/Contests/Practice/Index/152#11
# There is test that is not handled valid: Cannot have speed under 0

a = float(input())
result = 'Invalid Speed Entrance!'

if 0 <= a <= 10:
    result = 'slow'
elif 10 < a <= 50:
    result = 'average'
elif 50 < a <= 150:
    result = 'fast'
elif 150 < a <= 1000:
    result = 'ultra fast'
elif 1000 < a:
    result = 'extremely fast'

print(result)
