movie_name = input()
count = 0
ticket = ""
all_tickets = 0
student_count= 0
standard_count= 0
kid_count= 0




while movie_name != "Finish":
    number_seats = int(input())
    free_seats = number_seats

    while free_seats != 0:
        ticket = input()
        if ticket == "End":
            break
        count += 1
        all_tickets += 1
        free_seats -= 1

        if ticket == "student":
            student_count +=1
        elif ticket == "standard":
            standard_count +=1
        elif ticket == "kid":
            kid_count += 1

    hall_how_full = count / number_seats * 100
    print(f"{movie_name} - {hall_how_full:.2f}% full.")
    count = 0

    movie_name = input()

print(f"Total tickets: {all_tickets}")
percent_student_tickets = student_count / all_tickets * 100
print(f"{percent_student_tickets:.2f}% student tickets.")
percent_standard_tickets = standard_count / all_tickets * 100
print(f"{percent_standard_tickets:.2f}% standard tickets.")
percent_kid_tickets = kid_count / all_tickets * 100
print(f"{percent_kid_tickets:.2f}% kids tickets.")