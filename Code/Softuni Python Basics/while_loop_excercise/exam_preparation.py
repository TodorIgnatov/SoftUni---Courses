allowed_bad_marks = int(input())
bad_mark_counter = 0
average_score = 0
number_of_problems = 0
has_failed = True

while bad_mark_counter < allowed_bad_marks:
    name_of_problem = input()

    if name_of_problem == "Enough":
        has_failed = False
        break

    mark = int(input())

    if mark <= 4:
        bad_mark_counter +=1

    average_score += mark
    number_of_problems += 1
    last_problem = name_of_problem

if has_failed:
    print(f"You need a break, {bad_mark_counter} poor grades.")
else:
    average_score = average_score / number_of_problems
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")
