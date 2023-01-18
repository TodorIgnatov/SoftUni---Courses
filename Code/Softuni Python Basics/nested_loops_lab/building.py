number_floors = int(input())
number_apartments = int(input())
floor = number_floors

for i in range(number_floors, 0, -1):
    for j in range(number_apartments):
        if floor == number_floors:
            type_of_flat = f"L{i}{j}"
            # print(f"L{i}{j}", end=" ")
        elif floor % 2 == 0:
            type_of_flat = f"O{i}{j}"
            # print(f"O{i}{j}", end=" ")
        elif floor % 2 != 0:
            type_of_flat = f"A{i}{j}"
            # print(f"A{i}{j}", end=" ")

        print(type_of_flat, end=" ")

    print()

    floor -= 1