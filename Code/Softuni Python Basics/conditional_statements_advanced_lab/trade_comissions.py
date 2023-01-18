town = input()
sales_volume = float(input())
comission = 0

if town == "Sofia":
    if 0 <= sales_volume <= 500:
        comission = 0.05 * sales_volume
    if 500 < sales_volume <= 1000:
        comission = 0.07 * sales_volume
    if 1000 < sales_volume <= 10000:
        comission = 0.08 * sales_volume
    if 10000 < sales_volume:
        comission = 0.12 * sales_volume
elif town == "Varna":
    if 0 <= sales_volume <= 500:
        comission = 0.045 * sales_volume
    if 500 < sales_volume <= 1000:
        comission = 0.075 * sales_volume
    if 1000 < sales_volume <= 10000:
        comission = 0.1 * sales_volume
    if 10000 < sales_volume:
        comission = 0.13 * sales_volume
elif town == "Plovdiv":
    if 0 <= sales_volume <= 500:
        comission = 0.055 * sales_volume
    if 500 < sales_volume <= 1000:
        comission = 0.08 * sales_volume
    if 1000 < sales_volume <= 10000:
        comission = 0.12 * sales_volume
    if 10000 < sales_volume:
        comission = 0.145 * sales_volume


if town not in ["Sofia", "Varna", "Plovdiv"] or sales_volume < 0:
    print("error")
else:
    print(f"{comission:.2f}")