with open('inputs/day_01.txt') as input_file:
    lines = input_file.readlines()

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
