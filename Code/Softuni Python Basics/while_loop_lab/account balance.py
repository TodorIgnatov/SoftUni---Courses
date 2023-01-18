total = 0

while True:
    vnoska = input()

    if vnoska == "NoMoreMoney":
        break

    vnoska = float(vnoska)

    if vnoska > 0:
        print (f"Increase: {vnoska:.2f}")
    if vnoska < 0:
        print("Invalid operation!")
        break

    total += vnoska

print(f"Total: {total:.2f}")

