with open('inputs/day_02.txt') as input_file:
    rounds = input_file.readlines()

# part 1
score_map = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
total_score = 0

for round in rounds:
    total_score += score_map.get(round.strip())

print(f"Part 1 total score: {total_score}")

# part 2
score_map = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

total_score = 0
for round in rounds:
    total_score += score_map.get(round.strip())

print(f"Part 2 total score: {total_score}")
