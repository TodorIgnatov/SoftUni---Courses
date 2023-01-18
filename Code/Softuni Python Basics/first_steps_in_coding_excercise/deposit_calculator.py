deposit_sum = float(input())
deposit_term = int(input())
year_interest_rate = float(input())

per_year = deposit_sum * year_interest_rate/100
per_month = per_year / 12
total = deposit_sum + per_month * deposit_term

print(total)