budget = int(input())
season = input()
number_fishers = int(input())
price_rent = 0

if season == "Spring":
    price_rent = 3000
elif season == "Summer" or season == "Autumn":
    price_rent = 4200
elif season == "Winter":
    price_rent = 2600

if 0 < number_fishers <= 6:
    price_rent = price_rent * 0.9
elif 7 < number_fishers <= 11:
    price_rent = price_rent * 0.85
elif number_fishers >= 12:
    price_rent= price_rent * 0.75

if number_fishers % 2 == 0 and season != "Autumn":
    price_rent = price_rent * 0.95

diff = abs(budget - price_rent)

if budget >= price_rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")