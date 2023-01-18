import math

number_tournament = int(input())
starting_points = int(input())
points = 0
n = 0

for i in range(number_tournament):
    tournament_stage = input()
    if tournament_stage == "W":
        points += 2000
        n += 1
    elif tournament_stage == "F":
        points += 1200
    elif tournament_stage == "SF":
        points += 720

all_points = points + starting_points
print(f"Final points: {all_points}")

average_points = math.floor(points / number_tournament)
print(f"Average points: {average_points}")

won_tournaments = n / number_tournament * 100
print(f"{won_tournaments:.2f}%")

