chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price_chicken = chicken_menus * 10.35
price_fish = fish_menus * 12.40
price_vegetarian = vegetarian_menus * 8.15

sum_prices = price_fish + price_vegetarian + price_chicken
desert = 0.2 * sum_prices
delivery = 2.50
total = sum_prices + desert + delivery

print(total)