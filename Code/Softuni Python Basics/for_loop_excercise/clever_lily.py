age = int(input())
wm_price = float(input())
toy_price = int(input())
money_bd = 0
number_toys = 0
n = 0
money_bd_sum = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money_bd += 10
        money_bd_sum += money_bd
        n += 1
    else:
        number_toys += 1

money_brother = money_bd_sum - n
toy_money = number_toys * toy_price
total_sum = money_brother + toy_money
diff = abs(wm_price - total_sum)

if total_sum >= wm_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")


