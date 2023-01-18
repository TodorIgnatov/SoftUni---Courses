init_hour = int(input())
init_min = int(input())

total_time_min = (init_hour * 60) + init_min +15

hour = total_time_min // 60
minute = total_time_min % 60

if hour > 23:
    hour = hour - 24

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")