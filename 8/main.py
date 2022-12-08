import math


def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def tree_is_hidden(grid, pos):
    y, x = pos
    y_len = len(grid)
    x_len = len(grid[0])
    hidden_top = False
    hidden_bot = False
    hidden_left = False
    hidden_right = False
    hidden = False

    for i in range(y_len):
        if i == y:
            continue
        if grid[y][x] <= grid[i][x]:
            if i < y:
                hidden_top = True
            else:
                hidden_bot = True
            if hidden_top and hidden_bot:
                break

    for i in range(x_len):
        if i == x:
            continue
        if grid[y][x] <= grid[y][i]:
            if i < x:
                hidden_left = True
            else:
                hidden_right = True
            if hidden_right and hidden_left:
                break
    if hidden_left and hidden_right and hidden_top and hidden_bot:
        hidden = True

    return hidden


def get_visible_trees_sum(grid):
    visible = 0
    y_len = len(grid)
    x_len = len(grid[0])
    for y in range(y_len):
        x_len = len(grid[y])
        for x in range(x_len):
            hidden = False

            if y == 0 or y == y_len - 1:
                visible += 1
                continue
            if x == 0 or x == x_len - 1:
                visible += 1
                continue

            hidden = tree_is_hidden(grid, [y, x])
            if not hidden:
                visible += 1

    return visible


def get_viewing_distance(grid, pos, direction):
    y, x = pos
    score = 0
    match direction:
        case "left":
            i = x
            while i > 0:
                if grid[y][x] > grid[y][i - 1]:
                    score += 1
                else:
                    score += 1
                    break
                i -= 1
        case "right":
            i = x
            x_len = len(grid[0])
            while i < x_len - 1:
                if grid[y][x] > grid[y][i + 1]:
                    score += 1
                else:
                    score += 1
                    break
                i += 1
            i = y
        case "top":
            i = y
            while i > 0:
                if grid[y][x] > grid[i - 1][x]:
                    score += 1
                else:
                    score += 1
                    break
                i -= 1
        case "bot":
            i = y
            y_len = len(grid)
            while i < y_len - 1:
                if grid[y][x] > grid[i + 1][x]:
                    score += 1
                else:
                    score += 1
                    break
                i += 1
            i = y

    return score


def get_best_tree(grid):
    top_score = 0
    y_len = len(grid)
    x_len = len(grid[0])
    for y in range(y_len):
        x_len = len(grid[y])
        for x in range(x_len):
            score_map = {
                "left": 0,
                "right": 0,
                "top": 0,
                "bot": 0
            }
            if y == 0 or y == y_len - 1:
                continue
            if x == 0 or x == x_len - 1:
                continue
            score_map['left'] += get_viewing_distance(grid, [y, x], "left")
            score_map['right'] += get_viewing_distance(grid, [y, x], "right")
            score_map['top'] += get_viewing_distance(grid, [y, x], "top")
            score_map['bot'] += get_viewing_distance(grid, [y, x], "bot")

            score = math.prod(score_map.values())
            if score > top_score:
                top_score = score

    return top_score


def main():
    grid = []
    with open("input.lst") as f:
        for line in f:
            line = line.strip()
            temp_list = []
            for c in line:
                temp_list.append(c)
            grid.append(temp_list)

    p1 = get_visible_trees_sum(grid)
    p2 = get_best_tree(grid)
    print_solution(8, p1, p2)


if __name__ == "__main__":
    main()
