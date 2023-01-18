fats = int(input())
proteins = int(input())
carbs = int(input())
total_calories = int(input())
water_content = int(input())

grams_fat = float(fats * total_calories / 9 / 100)
grams_proteins = float(proteins * total_calories / 4 / 100)
grams_carbs = float(carbs * total_calories / 4 / 100)

food_weight = grams_fat + grams_proteins + grams_carbs
calories_per_gram = float(total_calories / food_weight)

water = water_content * calories_per_gram / 100

dry_calories = calories_per_gram - water
print(f"{dry_calories:.4f}")