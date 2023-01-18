needed_trip_money = float(input())
available_money = float(input())
num_days_spend = 0
num_days_save = 0
consecutive_counter = 0

while True:
    action = input()
    money_to_spend_save = float(input())
    if action == "spend":
        num_days_spend += 1
        available_money -= money_to_spend_save
        if available_money < 0:
            available_money = 0
        consecutive_counter += 1


    if action == "save":
        num_days_save += 1
        available_money += money_to_spend_save
        consecutive_counter = 0

    total_days = num_days_spend + num_days_save

    if available_money >= needed_trip_money:
        print(f"You saved the money for {total_days} days.")
        break
    if consecutive_counter == 5:
        print("You can't save the money.")
        print(f"{total_days}")
        break