with open('inputs/day_04.txt') as input_file:
    cleaning_assignments = input_file.readlines()

# part 1
pairs_for_reconsideration = 0

for assignment in cleaning_assignments:
    pair = assignment.strip().split(',')
    elf_1 = pair[0].split('-')
    elf_2 = pair[1].split('-')

    start_1 = int(elf_1[0])
    finish_1 = int(elf_1[1])
    start_2 = int(elf_2[0])
    finish_2 = int(elf_2[1])


    if start_1 <= start_2 and finish_1 >= finish_2:
        pairs_for_reconsideration += 1
    elif start_2 <= start_1 and finish_2 >= finish_1:
        pairs_for_reconsideration += 1

print(pairs_for_reconsideration)
