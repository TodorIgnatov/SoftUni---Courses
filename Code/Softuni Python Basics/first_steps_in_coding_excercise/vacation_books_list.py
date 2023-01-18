number_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

hours_total_book = number_pages // pages_per_hour
hours_per_day = hours_total_book // number_of_days

print(hours_per_day)