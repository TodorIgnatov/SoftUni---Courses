import math
n_days = int(input())
m_km_f_d = float(input())
total = m_km_f_d

for i in range(n_days):
    percent_per_day = int(input())
    x_day = m_km_f_d + m_km_f_d * percent_per_day /100
    m_km_f_d = x_day
    total += x_day


if total < 1000:
    diff = math.ceil(1000 - total)
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")
else:
    diff = math.ceil(total - 1000)
    print(f"You've done a great job running {diff} more kilometers!")