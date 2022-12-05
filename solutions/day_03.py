with open('inputs/day_03.txt') as input_file:
    sacks = input_file.readlines()

priorities = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z",
]
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
