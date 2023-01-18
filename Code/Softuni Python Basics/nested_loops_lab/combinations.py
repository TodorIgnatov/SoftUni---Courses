sum = int(input())
number_solutions = 0

for i in range(sum+1):
    for j in range(sum+1):
        for n in range(sum+1):
            if i + j + n == sum:
                number_solutions += 1

print(number_solutions)