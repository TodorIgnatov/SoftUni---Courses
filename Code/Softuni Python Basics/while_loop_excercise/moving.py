width = int(input())
length = int(input())
hight = int(input())
free_volume = width * length * hight

while free_volume > 0:
    number_boxes = input()

    if number_boxes == "Done":
        break

    number_boxes = int(number_boxes)
    free_volume -= number_boxes

if free_volume > 0:
    print(f"{free_volume} Cubic meters left.")
elif free_volume <= 0:
    print(f"No more free space! You need {abs(free_volume)} Cubic meters more.")

