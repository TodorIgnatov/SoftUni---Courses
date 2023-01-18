nailon_needed = int(input())
paint_needed = int(input())
disp_needed = int(input())
hours_workers = int(input())

sum_nailon = (nailon_needed + 2) * 1.50
sum_paint = paint_needed * 1.10 * 14.50
sum_disp = disp_needed * 5.00
sum_bags = 0.40

total_materials = sum_nailon + sum_paint + sum_disp +sum_bags
sum_workers = 0.3 * total_materials * hours_workers
total_sum = (total_materials + sum_workers)

print(total_sum)



