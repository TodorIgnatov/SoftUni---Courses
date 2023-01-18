import sys
minimum = sys.maxsize

while True:
    number = input()

    if number == "Stop":
        break

    number = int(number)
    if number < minimum:
        minimum = number

print(minimum)