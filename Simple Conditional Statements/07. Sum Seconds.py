# https://judge.softuni.bg/Contests/Practice/Index/152#6

time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

minutes = (time_1 + time_2 + time_3) // 60
seconds = (time_1 + time_2 + time_3) % 60

print(str(minutes) + ':' + '%02d' % seconds)
# Other solution
# print(str(minutes) + ':' + str(seconds).zfill(2))

