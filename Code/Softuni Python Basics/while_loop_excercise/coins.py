resto = float(input())
resto = resto * 100
count = 0

while resto > 0:
    if resto >= 200:
        resto -= 200
    elif resto >= 100:
        resto -= 100
    elif resto >= 50:
        resto -= 50
    elif resto >= 20:
        resto -= 20
    elif resto >= 10:
        resto -= 10
    elif resto >= 5:
        resto -= 5
    elif resto >= 2:
        resto -= 2
    elif resto >= 1:
        resto -= 1
    else:
        break

    count += 1

print(count)



