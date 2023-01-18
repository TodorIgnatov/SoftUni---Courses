command = input()
count = 0
sum_prime = 0
sum_non_prime = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
    elif number > 0:
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1

    if count > 2:
        sum_non_prime += number
    elif count == 2:
        sum_prime += number

    count = 0

    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")