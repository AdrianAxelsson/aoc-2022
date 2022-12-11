def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def move_head(direction, pos):
    match direction:
        case "R":
            pos[0] += 1
        case "U":
            pos[1] += 1
        case "L":
            pos[0] -= 1
        case "D":
            pos[1] -= 1
    return pos


def move_tail(direction, tail_pos, head_pos):
    match direction:
        case "R":
            head_tail_diff = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
            if abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 0:
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 1:
                tail_pos[1] += head_tail_diff[1]
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[0]) == 1 and abs(head_tail_diff[1]) == 2:
                tail_pos[1] += head_tail_diff[1] // 2
                tail_pos[0] += head_tail_diff[0]
            elif abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 2:
                tail_pos[1] += head_tail_diff[1] // 2
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[0]) == 0 and abs(head_tail_diff[1]) == 2:
                tail_pos[1] += head_tail_diff[1] // 2

        case "U":
            head_tail_diff = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
            if abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 0:
                tail_pos[1] += 1
            elif abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 1:
                tail_pos[1] += head_tail_diff[1] // 2
                tail_pos[0] += head_tail_diff[0]
            elif abs(head_tail_diff[1]) == 1 and abs(head_tail_diff[0]) == 2:
                tail_pos[1] += head_tail_diff[1]
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 2:
                tail_pos[1] += head_tail_diff[1] // 2
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[1]) == 0 and abs(head_tail_diff[0]) == 2:
                tail_pos[0] += head_tail_diff[0] // 2

        case "L":
            head_tail_diff = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
            if abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 0:
                tail_pos[0] += head_tail_diff[0] // 2
            elif abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 1:
                tail_pos[0] += head_tail_diff[0] // 2
                tail_pos[1] += head_tail_diff[1]
            elif abs(head_tail_diff[0]) == 1 and abs(head_tail_diff[1]) == 2:
                tail_pos[0] += head_tail_diff[0]
                tail_pos[1] += head_tail_diff[1] // 2
            elif abs(head_tail_diff[0]) == 2 and abs(head_tail_diff[1]) == 2:
                tail_pos[0] += head_tail_diff[0] // 2
                tail_pos[1] += head_tail_diff[1] // 2
            elif abs(head_tail_diff[0]) == 0 and abs(head_tail_diff[1]) == 2:
                tail_pos[1] += head_tail_diff[1] // 2

        case "D":
            head_tail_diff = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
            if abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 0:
                tail_pos[1] += head_tail_diff[1] // 2
            elif abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 1:
                tail_pos[0] += head_tail_diff[0]
                tail_pos[1] += head_tail_diff[1] // 2
            elif abs(head_tail_diff[1]) == 1 and abs(head_tail_diff[0]) == 2:
                tail_pos[0] += head_tail_diff[0] // 2
                tail_pos[1] += head_tail_diff[1]
            elif abs(head_tail_diff[1]) == 2 and abs(head_tail_diff[0]) == 2:
                tail_pos[0] += head_tail_diff[0] // 2
                tail_pos[1] += head_tail_diff[1] // 2
            elif abs(head_tail_diff[1]) == 0 and abs(head_tail_diff[0]) == 2:
                tail_pos[0] += head_tail_diff[0] // 2

    return tail_pos


def main():
    knots = [[0, 0] for _ in range(10)]
    tail_visits = set()
    knot1_visits = set()
    with open("input.lst") as f:
        for line in f:
            line = line.strip()
            direction, amount = line.split()
            for i in range(int(amount)):
                move_head(direction, knots[0])
                for j in range(len(knots) - 1):
                    move_tail(direction, knots[j + 1], knots[j])

                knot1_visits.add(str(knots[1]))
                tail_visits.add(str(knots[9]))

    p1 = len(knot1_visits)
    p2 = len(tail_visits)
    print_solution(9, p1, p2)


if __name__ == "__main__":
    main()
