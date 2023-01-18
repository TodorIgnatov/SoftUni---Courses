import sys
maximum = -sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break

    number = int(number)
    if number > maximum:
        maximum = number

print(maximum)