with open("inputs/day_05.txt") as input_file:
    instructions = input_file.readlines()


"""
Starting Arrangement

[G]                 [D] [R]
[W]         [V]     [C] [T] [M]
[L]         [P] [Z] [Q] [F] [V]
[J]         [S] [D] [J] [M] [T] [V]
[B]     [M] [H] [L] [Z] [J] [B] [S]
[R] [C] [T] [C] [T] [R] [D] [R] [D]
[T] [W] [Z] [T] [P] [B] [B] [H] [P]
[D] [S] [R] [D] [G] [F] [S] [L] [Q]
 1   2   3   4   5   6   7   8   9
"""

# part 1
crates = {
    "1": ["D", "T", "R", "B", "J", "L", "W", "G"],
    "2": ["S", "W", "C"],
    "3": ["R", "Z", "T", "M"],
    "4": ["D", "T", "C", "H", "S", "P", "V"],
    "5": ["G", "P", "T", "L", "D", "Z"],
    "6": ["F", "B", "R", "Z", "J", "Q", "C", "D"],
    "7": ["S", "B", "D", "J", "M", "F", "T", "R"],
    "8": ["L", "H", "R", "B", "T", "V", "M"],
    "9": ["Q", "P", "D", "S", "V"],
}

for step in instructions:
    step = step.strip().split(" ")

    move_num = int(step[1])
    move_from = step[3]
    move_to = step[5]

    for _ in range(move_num):
        crates[move_to].append(crates[move_from].pop())

final_message = ""
for i in range(len(crates)):
    i += 1
    final_message += crates[str(i)][-1]

print(f"final message: {final_message}")

# part 2
crates = {
    "1": ["D", "T", "R", "B", "J", "L", "W", "G"],
    "2": ["S", "W", "C"],
    "3": ["R", "Z", "T", "M"],
    "4": ["D", "T", "C", "H", "S", "P", "V"],
    "5": ["G", "P", "T", "L", "D", "Z"],
    "6": ["F", "B", "R", "Z", "J", "Q", "C", "D"],
    "7": ["S", "B", "D", "J", "M", "F", "T", "R"],
    "8": ["L", "H", "R", "B", "T", "V", "M"],
    "9": ["Q", "P", "D", "S", "V"],
}

for step in instructions:
    step = step.strip().split(" ")

    move_num = int(step[1])
    move_from = step[3]
    move_to = step[5]

    temp_stack = crates[move_from][-move_num:]
    del crates[move_from][-move_num:]

    crates[move_to].append(temp_stack)

    flat_list = []
    for sublist in crates[move_to]:
        for item in sublist:
            flat_list.append(item)

    crates[move_to] = flat_list

final_message = ""
for i in range(len(crates)):
    i += 1
    final_message += crates[str(i)][-1]

print(f"final message: {final_message}")
