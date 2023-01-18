number = int(input())

for i in range(1111, 10000):
    first = i // 1000
    second = (i // 100) % 10
    third = (i // 10) % 10
    fourth = i % 10

    if first == 0 or second == 0 or third == 0 or fourth == 0:
        continue

    if number % first == 0 and number % second == 0 and number % third == 0 and number % fourth == 0:
        print(i, end=" ")






