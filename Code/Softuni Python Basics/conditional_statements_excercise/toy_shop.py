trip_price = float(input())
num_puzzles = int(input())
num_dolls = int(input())
num_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

number_of_toys = num_puzzles + num_dolls + num_bears + num_minions + num_trucks
total_amount = num_puzzles * 2.60 + num_dolls * 3 + num_bears * 4.10 + num_minions * 8.20 + num_trucks * 2

if number_of_toys >= 50:
    total_amount = total_amount - total_amount * 0.25

total_amount = total_amount - total_amount * 0.1

difference = abs(total_amount - trip_price)

if trip_price <= total_amount:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
