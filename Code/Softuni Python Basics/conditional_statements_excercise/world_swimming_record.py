import math

record_to_beat = float(input())
distance = float(input())
time_for_1m = float(input())

time_for_distance = distance * time_for_1m

latency = math.floor(distance / 15) * 12.5

total_time = time_for_distance + latency

if total_time < record_to_beat:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_to_beat
    print(f"No, he failed! He was {diff:.2f} seconds slower.")