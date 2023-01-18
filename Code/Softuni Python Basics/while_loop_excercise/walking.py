all_steps = 0
steps_to_home = 0

while all_steps <= 10000:
    steps = input()

    if steps == "Going home":
        steps_to_home = int(input())
        all_steps += steps_to_home
        break

    steps = int(steps)

    all_steps += steps

diff = abs(all_steps - 10000)

if all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

