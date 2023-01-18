start_number = int(input())
stop_number = int(input())
magic_number = int(input())
counter = 0
flag = False

for i in range(start_number, stop_number+1):
    for j in range(start_number, stop_number+1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            flag = True
            break
    if flag:
        break


if flag == False:
    print(f"{counter} combinations - neither equals {magic_number}")
