with open('inputs/day_01.txt') as input_file:
    lines = input_file.readlines()

# part 1
max_calories = 0
total_calories = 0

for line in lines:
    cals = line.strip()
    if cals == "":
        if total_calories > max_calories:
            max_calories = total_calories
        total_calories = 0
        continue
    else:
        total_calories += int(cals)

print(max_calories)

# part 2
total_calories_top_3 = 0
individual_calorie_counter = 0
calorie_totals = []

for line in lines:
    cals = line.strip()
    if cals == "":
        calorie_totals.append(individual_calorie_counter)
        individual_calorie_counter = 0
        continue
    else:
        individual_calorie_counter += int(cals)

calorie_totals.sort(reverse=True)
print(sum(calorie_totals[0:3]))
