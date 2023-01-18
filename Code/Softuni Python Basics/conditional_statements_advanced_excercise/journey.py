budget = float(input())
season = input()

destination = ""
money_spent = 0
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        money_spent = 0.3 *budget
    elif season == "winter":
        place = "Hotel"
        money_spent = 0.7 * budget
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        money_spent = 0.4 *budget
    elif season == "winter":
        place = "Hotel"
        money_spent = 0.8 * budget
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    money_spent = budget * 0.9


print(f"Somewhere in {destination}")
print(f"{place} - {money_spent:.2f}")

