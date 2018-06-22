# https://judge.softuni.bg/Contests/Practice/Index/152#6

time_1 = int(input())
time_2 = int(input())
time_3 = int(input())
sum_time = time_1 + time_2 + time_3

minutes = sum_time // 60
seconds = sum_time % 60

print(str(minutes) + ':' + '%02d' % seconds)
# Other solution
# print(str(minutes) + ':' + str(seconds).zfill(2))
