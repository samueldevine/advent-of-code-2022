with open('inputs/day_01.txt') as input_file:
    lines = input_file.readlines()

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

# part 1 answer
print(calorie_totals[0])

# part 2 answer
print(sum(calorie_totals[0:3]))
