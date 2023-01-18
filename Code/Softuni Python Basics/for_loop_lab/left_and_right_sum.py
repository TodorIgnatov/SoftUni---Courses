n = int(input())
N = 2 * n
left_sum = 0
right_sum = 0

for i in range(N-n):
    a = int(input())
    left_sum += a

for i in range(N-n, N):
    b = int(input())
    right_sum += b

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")
