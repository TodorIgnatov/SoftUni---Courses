type_flowers = input()
number_flowers = int(input())
budged = int(input())

price = 0

if type_flowers == "Roses":
    price = number_flowers * 5
    if number_flowers > 80:
        price = price - price * 0.10
elif type_flowers == "Dahlias":
    price = number_flowers * 3.80
    if number_flowers > 90:
        price = price - price * 0.15
elif type_flowers == "Tulips":
    price = number_flowers * 2.80
    if number_flowers > 80:
        price = price - price * 0.15
elif type_flowers == "Narcissus":
    price = number_flowers * 3
    if number_flowers < 120:
        price = price + price * 0.15
elif type_flowers == "Gladiolus":
    price = number_flowers * 2.50
    if number_flowers < 80:
        price = price + price * 0.20

diff = (budged - price)

if diff >= 0:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(diff):.2f} leva more.")


