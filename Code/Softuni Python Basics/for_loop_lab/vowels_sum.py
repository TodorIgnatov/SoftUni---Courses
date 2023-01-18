text = input()
value = 0

for ch in text:
    if ch == "a":
        value = value + 1
    elif ch == "e":
        value = value + 2
    elif ch == "i":
        value = value + 3
    elif ch == "o":
        value = value + 4
    elif ch == "u":
        value = value + 5

print(value)