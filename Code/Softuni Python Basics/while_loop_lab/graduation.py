name  = input()
average_mark = 0
failed_year = 0
years_counter = 0

while True:
    mark = float(input())
    years_counter += 1

    if mark < 4:
        failed_year += 1
        if failed_year == 2:
            print(f"{name} has been excluded at {years_counter} grade")
            break
        years_counter -= 1
    else:
        average_mark += mark


    if years_counter == 12:
        average_mark = average_mark / 12
        print(f"{name} graduated. Average grade: {average_mark:.2f}")
        break


