n = int(input())
flag = False

for a in range(1, 10):
    for b in range(9, a-1, -1):
        for c in range(10):
            for d in range(9, c-1, -1):

                y = a * b * c * d / (a + b + c + d)

                if a+b+c+d == a*b*c*d:
                    if n % 10 == 5:
                        print(f"{a}{b}{c}{d}")
                        flag = True
                        break

                if int(y) == 3:
                    if n % 3 == 0:
                        print(f"{d}{c}{b}{a}")
                        flag = True
                        break


            if flag:
                break
        if flag:
            break
    if flag:
        break



if not(flag):
    print("Nothing found")
