def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def find_start_marker(datastream, message=False):
    j = 14 if message else 4
    for i in (range(len(datastream))):
        if len(set(datastream[i:i+j])) == j:
            return i + j
    return False


def main():
    with open("input.lst") as f:
        line = f.read()
    p1 = find_start_marker(line)
    p2 = find_start_marker(line, message=True)

    print_solution(6, p1, p2)


if __name__ == "__main__":
    main()
