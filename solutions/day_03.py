with open('inputs/day_03.txt') as input_file:
    sacks = input_file.readlines()

priorities = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z",
]

# part 1

sum_of_priorities = 0
for sack in sacks:
    sack = sack.strip()
    midpoint_index = int(len(sack) / 2)
    compartment_1 = sack[0:midpoint_index]
    compartment_2 = sack[midpoint_index:]
    repeated_item = ''.join(set(compartment_1).intersection(compartment_2))

    priority = priorities.index(repeated_item) + 1

    sum_of_priorities += priority

print(sum_of_priorities)

# part 2

sum_of_priorities = 0
elf_1 = 0

for sack in sacks:
    if elf_1 >= len(sacks) - 1:
        break

    sack_1 = sacks[elf_1].strip()
    sack_2 = sacks[elf_1 + 1].strip()
    sack_3 = sacks[elf_1 + 2].strip()

    badge = ''.join(set(sack_1) & set(sack_2) & set(sack_3))
    priority = priorities.index(badge) + 1
    sum_of_priorities += priority

    elf_1 += 3

print(sum_of_priorities)
