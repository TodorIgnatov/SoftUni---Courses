import sys

n = int(input())
sum = 0
max_num = -sys.maxsize

for i in range(n):
    current_num = int(input())
    sum += current_num
    if current_num > max_num:
        max_num = current_num


if max_num == sum - max_num:
    print("Yes")
    print(f"Sum = {abs(sum-max_num)}")
else:
    diff = abs(max_num - (sum - max_num))
    print("No")
    print(f"Diff = {diff}")



