# https://judge.softuni.bg/Contests/Practice/Index/368#0

initial_velocity = int(input())
first_time = int(input())
second_time = int(input())
third_time = int(input())

first_distance = initial_velocity * first_time / 60
second_distance = initial_velocity * second_time / 60 * 1.1
third_distance = initial_velocity * 1.1 * 0.95 * third_time / 60
result = (first_distance + second_distance + third_distance)

# print(first_distance)
# print(second_distance)
# print(third_distance)
print(f'{result:.2f}')
