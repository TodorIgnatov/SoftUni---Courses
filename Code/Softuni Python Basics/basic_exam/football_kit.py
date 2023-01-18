tshirt_price = float(input())
sum_for_ball = float(input())

shorts_price = 0.75 * tshirt_price
socks_price = 0.2 * shorts_price
shoes_price = 2 * (tshirt_price + shorts_price)

total_sum = tshirt_price + shorts_price + socks_price + shoes_price
total_sum_after_discount = total_sum - total_sum * 0.15

if total_sum_after_discount >= sum_for_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum_after_discount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    diff = sum_for_ball - total_sum_after_discount
    print(f"He needs {diff:.2f} lv. more.")