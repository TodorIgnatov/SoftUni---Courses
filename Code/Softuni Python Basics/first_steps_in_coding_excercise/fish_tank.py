length = int(input())
width = int(input())
hight = int(input())
percent = float(input())

all_liters = ((length * width * hight)/1000)
actual_leters = all_liters - (percent/100*all_liters)

print(actual_leters)



