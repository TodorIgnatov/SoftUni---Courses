import math

name_of_series = input()
duration_series = int(input())
duration_break = int(input())

time_lunch = 1/8 * duration_break
time_relax = 1/4 * duration_break
time_left = duration_break - time_lunch - time_relax

diff = math.ceil(abs(time_left - duration_series))

if time_left >= duration_series:
    print(f"You have enough time to watch {name_of_series} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {diff} more minutes.")

