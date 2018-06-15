# https://judge.softuni.bg/Contests/Practice/Index/1#3

# Input
guessed_number = int(4268)
# bulls = int(input())
# cows = int(input())

# Decide the number
# We need to define based on the guess_number what exactly are numbers.


# Returns the value at specific position in number
def get_position(number, position):
    for a in range(position):
        tmp = number % 10
        number = number // 10
    return tmp


n1 = get_position(guessed_number, 1)
n10 = get_position(guessed_number, 2)
n100 = get_position(guessed_number, 3)
n1000 = get_position(guessed_number, 4)
print(n1, n10, n100, n1000)
# Iteration and print
for i in range(0, 10000):
    print(str(i), end=' ')
    i += 1

