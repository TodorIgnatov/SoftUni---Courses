pens_packages = int(input())
markers_packages = int(input())
liters_cleaner = int(input())
percentage_discount = int(input())

price_pens = pens_packages * 5.80
price_markers = markers_packages * 7.20
price_cleaner = liters_cleaner * 1.20
sum = price_pens +price_markers + price_cleaner
discount = sum * percentage_discount/100
total = sum - discount

print (total)
