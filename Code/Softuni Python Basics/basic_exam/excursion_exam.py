number_people = int(input())
season = input()

if number_people <= 5 and season == "spring":
    price = number_people * 50
    print(f"{price:.2f} leva.")

elif number_people <= 5 and season == "summer":
    price = number_people * 48.50 * 0.85
    print(f"{price:.2f} leva.")

elif number_people <= 5 and season == "autumn":
    price = number_people * 60
    print(f"{price:.2f} leva.")

elif number_people <= 5 and season == "winter":
    price = number_people * 86 * 1.08
    print(f"{price:.2f} leva.")

if number_people > 5 and season == "spring":
    price = number_people * 48
    print(f"{price:.2f} leva.")

elif number_people > 5 and season == "summer":
    price = number_people * 45 * 0.85
    print(f"{price:.2f} leva.")

elif number_people > 5 and season == "autumn":
    price = number_people * 49.50
    print(f"{price:.2f} leva.")

elif number_people > 5 and season == "winter":
    price = number_people * 85 * 1.08
    print(f"{price:.2f} leva.")