number_tabs = int(input())
salary = int(input())
fine = 0

for i in range(number_tabs, 0, -1):
    tab_name = input()
    if tab_name == "Facebook":
        salary = salary - 150
        fine += 150
    elif tab_name == "Instagram":
        salary = salary - 100
        fine += 100
    elif tab_name == "Reddit":
        salary = salary - 50
        fine += 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)