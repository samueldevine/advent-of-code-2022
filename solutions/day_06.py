with open("inputs/day_06.txt") as input_file:
    stream = input_file.read()

chars = list(stream)

# part 1
counter = 0
last_4 = ["r", "r", "r", "r"]

for char in chars:
    if len(set(last_4)) == len(last_4):
        break

    last_4.append(char)
    del last_4[0]
    counter += 1

print(last_4)
print(counter)

# part 2
counter = 0
last_14 = ["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"]

for char in chars:
    if len(set(last_14)) == len(last_14):
        break

    last_14.append(char)
    del last_14[0]
    counter += 1

print(last_14)
print(counter)
