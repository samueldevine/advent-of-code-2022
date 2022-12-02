with open('inputs/day_02.txt') as input_file:
    rounds = input_file.readlines()

scores = {"X": 1, "Y": 2, "Z": 3, "loss": 0, "draw": 3, "win": 6}
total_score = 0

for round in rounds:
    opponent = round[0]
    my_play = round[2]
    if my_play == "X": # rock
        total_score += scores["X"]
        if opponent == "A": # rock
            total_score += scores["draw"]
        if opponent == "B": # paper
            total_score += scores["loss"]
        if opponent == "C": # scissors
            total_score += scores["win"]
    if my_play == "Y": # paper
        total_score += scores["Y"]
        if opponent == "A": # rock
            total_score += scores["win"]
        if opponent == "B": # paper
            total_score += scores["draw"]
        if opponent == "C": # scissors
            total_score += scores["loss"]
    if my_play == "Z": # scissors
        total_score += scores["Z"]
        if opponent == "A": # rock
            total_score += scores["loss"]
        if opponent == "B": # paper
            total_score += scores["win"]
        if opponent == "C": # scissors
            total_score += scores["draw"]

print(f"Part 1 total score: {total_score}")

# part 2
loss_map = {"A": 3, "B": 1, "C": 2}
draw_map = {"A": 4, "B": 5, "C": 6}
win_map = {"A": 8, "B": 9, "C": 7}

total_score = 0
for round in rounds:
    opponent = round[0]
    result = round[2]

    if result == "X": # loss
        total_score += loss_map[opponent]
    if result == "Y": # draw
        total_score += draw_map[opponent]
    if result == "Z": # win
        total_score += win_map[opponent]

print(f"Part 2 total score: {total_score}")
