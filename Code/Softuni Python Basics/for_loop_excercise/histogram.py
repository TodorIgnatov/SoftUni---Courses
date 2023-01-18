n = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in range(n):
    current_num = int(input())
    if current_num < 200:
        count1 += 1
    elif 200 <= current_num < 400:
        count2 += 1
    elif 400 <= current_num < 600:
        count3 += 1
    elif 600 <= current_num < 800:
        count4 += 1
    elif 800 <= current_num:
        count5 += 1

p1 = count1 / n *100
p2 = count2 / n *100
p3 = count3 / n *100
p4 = count4 / n *100
p5 = count5 / n *100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")