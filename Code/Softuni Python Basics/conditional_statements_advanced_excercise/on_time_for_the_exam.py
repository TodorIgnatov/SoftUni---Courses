hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_all_mins = hour_exam * 60 + minute_exam
arr_all_mins = hour_arrival * 60 + minute_arrival

if arr_all_mins > exam_all_mins:
    print("Late")
    if (arr_all_mins - exam_all_mins) >= 60:
        hour = (arr_all_mins - exam_all_mins) //60
        minutes = (arr_all_mins - exam_all_mins) % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        minutes = arr_all_mins - exam_all_mins
        print(f"{minutes} minutes after the start")
elif arr_all_mins == exam_all_mins or (exam_all_mins - arr_all_mins) <=30:
    print("On time")
    if (exam_all_mins - arr_all_mins) > 0:
        minutes = exam_all_mins - arr_all_mins
        print(f"{minutes} minutes before the start")
else:
    print("Early")
    if (exam_all_mins - arr_all_mins) >= 60:
        hour = (exam_all_mins - arr_all_mins) // 60
        minutes = (exam_all_mins - arr_all_mins) % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        minutes = (exam_all_mins - arr_all_mins) % 60
        print(f"{minutes} minutes before the start")

