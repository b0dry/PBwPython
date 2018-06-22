# https://judge.softuni.bg/Contests/Practice/Index/368#5

begin = input()
end = input()
skip = input()

counter = 0

while not (len(begin) == 1 and len(end) == 1 and len(skip) == 1):
    begin = input()
    end = input()
    skip = input()

for first_letter in range(ord(begin[0]), ord(end[0]) + 1):
    if not first_letter == ord(skip):
        for second_letter in range(ord(begin[0]), ord(end[0]) + 1):
            if not second_letter == ord(skip):
                for third_letter in range(ord(begin[0]), ord(end[0]) + 1):
                    if not third_letter == ord(skip):
                        print(chr(first_letter) + chr(second_letter) + chr(third_letter), end=' ')
                        counter += 1
print(counter)
