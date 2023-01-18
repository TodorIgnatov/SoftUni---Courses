length = int(input())
width = int(input())
number_pieces = length * width

while number_pieces > 0:
    taken_pieces = input()

    if taken_pieces == "STOP":
        print(f"{number_pieces} pieces are left." )
        break

    taken_pieces = int(taken_pieces)
    number_pieces -= taken_pieces

if number_pieces <= 0:
    print(f"No more cake left! You need {abs(number_pieces)} pieces more.")
