fruit = input()
day_of_week = input()
quantity = float(input())
price = 0

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = 2.50 * quantity
    elif fruit == "apple":
        price = 1.20 * quantity
    elif fruit == "orange":
        price = 0.85 * quantity
    elif fruit == "grapefruit":
        price = 1.45 * quantity
    elif fruit == "kiwi":
        price = 2.70 * quantity
    elif fruit == "pineapple":
        price = 5.50 * quantity
    elif fruit == "grapes":
        price = 3.85 * quantity
    else:
        print("error")
elif day_of_week in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = 2.70 * quantity
    elif fruit == "apple":
        price = 1.25 * quantity
    elif fruit == "orange":
        price = 0.90 * quantity
    elif fruit == "grapefruit":
        price = 1.60 * quantity
    elif fruit == "kiwi":
        price = 3.00 * quantity
    elif fruit == "pineapple":
        price = 5.60 * quantity
    elif fruit == "grapes":
        price = 4.20 * quantity
    else:
        print("error")
else:
    print("error")

if price != 0:
    print(f"{price:.2f}")