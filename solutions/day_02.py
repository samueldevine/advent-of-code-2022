with open('inputs/day_02.txt') as input_file:
    rounds = input_file.readlines()

scores = {"X": 1, "Y": 2, "Z": 3, "loss": 0, "draw": 3, "win": 6}
total_score = 0

for round in rounds:
    opponent = round[0]
    my_play = round[2]
    if my_play == "X":
        total_score += scores["X"]
        if opponent == "A":
            total_score += scores["draw"]
        if opponent == "B":
            total_score += scores["loss"]
        if opponent == "C":
            total_score += scores["win"]
    if my_play == "Y":
        total_score += scores["Y"]
        if opponent == "A":
            total_score += scores["win"]
        if opponent == "B":
            total_score += scores["draw"]
        if opponent == "C":
            total_score += scores["loss"]
    if my_play == "Z":
        total_score += scores["Z"]
        if opponent == "A":
            total_score += scores["loss"]
        if opponent == "B":
            total_score += scores["win"]
        if opponent == "C":
            total_score += scores["draw"]

print(total_score)
