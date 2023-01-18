jury_number = int(input())
presentation_name = input()
sum_marks = 0
sum_all_marks = 0
counter = 0

while presentation_name != "Finish":
    for i in range(jury_number):
        mark = float(input())
        sum_marks += mark
        counter += 1

    average_mark = sum_marks / jury_number

    print(f"{presentation_name} - {average_mark:.2f}.")

    sum_all_marks += sum_marks
    sum_marks = 0

    presentation_name = input()

final_assesment = sum_all_marks / counter

print(f"Student's final assessment is {final_assesment:.2f}.")
