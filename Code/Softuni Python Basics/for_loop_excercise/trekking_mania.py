number_of_groups = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for i in range(number_of_groups):
    number_people = int(input())
    if number_people <= 5:
        g1 += number_people
    elif 5 < number_people <= 12:
        g2 += number_people
    elif 12 < number_people <= 25:
        g3 += number_people
    elif 25 < number_people <= 40:
        g4 += number_people
    elif 40 < number_people:
        g5 += number_people

total_people = g1 + g2 +g3 + g4 + g5
p1 = g1 / total_people * 100
p2 = g2 / total_people * 100
p3 = g3 / total_people * 100
p4 = g4 / total_people * 100
p5 = g5 / total_people * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")