target = int(input())
command = input()
total_amount = 0

while command != "closed":
    if command == "haircut":
        type = input()
        if type == "mens":
            price = 15
        elif type == "ladies":
            price = 20
        elif type == "kids":
            price = 10
    elif command == "color":
        type = input()
        if type == "touch up":
            price = 20
        elif type == "full color":
            price = 30

    total_amount += price

    if total_amount >=target:
        break

    command = input()

if target <= total_amount:
    print("You have reached your target for the day!")
    print(f"Earned money: {total_amount}lv.")
else:
    diff = target - total_amount
    print(f"Target not reached! You need {diff}lv. more.")
    print(f"Earned money: {total_amount}lv.")

