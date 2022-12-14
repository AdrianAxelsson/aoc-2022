with open("input.lst") as f:
    input = f.read().splitlines()

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

def get_rounds():
    rounds = []
    for line in input:
        rounds.append(line.split(' '))
    return rounds

def play_round(round):
    opponent, me = round
    score = scores[me]
    if me == 'X':
        if opponent == 'A': score += 3
        elif opponent == 'B': score += 0
        elif opponent == 'C': score += 6
    elif me == 'Y':
        if opponent == 'A': score += 6
        elif opponent == 'B': score += 3
        elif opponent == 'C': score += 0
    elif me == 'Z':
        if opponent == 'A': score += 0
        elif opponent == 'B': score += 6
        elif opponent == 'C': score += 3
    return score

def play_round_p2(round):
    opponent, result = round
    if result == 'X':
        if opponent == 'A': me = 'C'
        elif opponent == 'B': me = 'A'
        elif opponent == 'C': me = 'B'
    elif result == 'Y':
        me = opponent
    elif result == 'Z':
        if opponent == 'A': me = 'B'
        elif opponent == 'B': me = 'C'
        elif opponent == 'C': me = 'A'

    score = scores[me]
    if me == 'A':
        if opponent == 'A': score += 3
        elif opponent == 'B': score += 0
        elif opponent == 'C': score += 6
    elif me == 'B':
        if opponent == 'A': score += 6
        elif opponent == 'B': score += 3
        elif opponent == 'C': score += 0
    elif me == 'C':
        if opponent == 'A': score += 0
        elif opponent == 'B': score += 6
        elif opponent == 'C': score += 3
    return score

rounds = get_rounds()

p1 = 0
for round in rounds:
    p1 += play_round(round)

p2 = 0
for round in rounds:
    p2 += play_round_p2(round)


print("** AoC 2022 - Day 2 Solution **")
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
