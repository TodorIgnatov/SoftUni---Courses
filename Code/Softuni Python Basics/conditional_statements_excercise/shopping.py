budget = float(input())
num_vcards = int(input())
num_processors = int(input())
num_ram = int(input())

price_vcards = num_vcards * 250
price_processors = price_vcards * 0.35 * num_processors
price_rams = price_vcards * 0.10 * num_ram
total_price = price_vcards + price_processors + price_rams

if num_vcards > num_processors:
    total_price = total_price - total_price * 0.15

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")