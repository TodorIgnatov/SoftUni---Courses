name = input()
points_academy = float(input())
number_critics = int(input())
total_points = 0

for i in range(number_critics):
    name_critic = input()
    points_critic = float(input())

    current_points = ((len(name_critic) * points_critic) / 2)
    total_points += current_points
    all_points = total_points + points_academy

    if all_points > 1250.5:
        print(f"Congratulations, {name} got a nominee for leading role with {all_points:.1f}!")
        break

if all_points <= 1250.5:
    diff = 1250.5 - all_points
    print(f"Sorry, {name} you need {diff:.1f} more!")