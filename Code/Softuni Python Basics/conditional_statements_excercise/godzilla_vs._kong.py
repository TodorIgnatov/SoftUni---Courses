budget = float(input())
stats = int(input())
price_dress_per_stat = float(input())
price_dress_all_stats = stats * price_dress_per_stat

decor = budget * 0.1

if stats > 150:
    price_dress_all_stats = price_dress_all_stats - price_dress_all_stats * 0.1

total_costs = price_dress_all_stats + decor

difference = abs(budget - total_costs)

if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")