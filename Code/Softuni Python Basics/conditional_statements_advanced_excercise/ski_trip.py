days = int(input())
room = input()
rating = input()
price = 0
nights = days - 1

if room == "room for one person":
    price = nights * 18.00
elif room == "apartment":
    price = nights * 25.00
    if days < 10:
        price = price * 0.7
    elif 10 <= days <= 15:
        price = price * 0.65
    elif days > 15:
        price = price * 0.5
elif room == "president apartment":
    price = nights * 35.00
    if days < 10:
        price = price * 0.9
    elif 10 <= days <= 15:
        price = price * 0.85
    elif days > 15:
        price = price * 0.8

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * 0.9

print(f"{price:.2f}")
