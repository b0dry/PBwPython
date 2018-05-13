# https://judge.softuni.bg/Contests/Practice/Index/169#2

hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_abs = hour_exam * 60 + minute_exam
arrival_abs = hour_arrival * 60 + minute_arrival

result = exam_abs - arrival_abs

if result == 0:
    print('On time')
elif 0 < result <= 30:
    print('On time')
    print(f'{result} minutes before the start')
elif 30 < result < 60:
    print('Early')
    print(f'{result} minutes before the start')
    # print('{0:.2f} minutes before the start'.format(result))
elif result >= 60:
    print('Early')
    print(f'{abs(result) // 60}:' + '{:02d} hours before the start'.format(abs(result) % 60))
elif 0 > result > -60:
    print('Late')
    print(f'{abs(result)} minutes after the start')
else:
    print('Late')
    print(f'{abs(result) // 60}:' + '{:02d} hours after the start'.format(abs(result) % 60))
