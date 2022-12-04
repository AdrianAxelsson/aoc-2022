def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def expand_assignment(assingment):
    expanded_assignment = set()
    start, stop = assingment.split("-")
    for i in range(int(start), int(stop) + 1):
        expanded_assignment.add(i)
    return expanded_assignment


def find_overlap(section_pair):
    s1, s2 = section_pair.split(",")
    s1_set = expand_assignment(s1)
    s2_set = expand_assignment(s2)
    set_intersection = s1_set.intersection(s2_set)
    if set_intersection == s1_set:
        return [1, 1]
    if set_intersection == s2_set:
        return [1, 1]
    if len(set_intersection) > 0:
        return [0, 1]
    return [0, 0]


def main():
    full_overlap_sum = 0
    any_overlap_sum = 0

    with open("input.lst") as f:
        for line in f:
            section_pair = line.split()[0]
            overlap = find_overlap(section_pair)
            full_overlap_sum += overlap[0]
            any_overlap_sum += overlap[1]

    print_solution(4, full_overlap_sum, any_overlap_sum)


if __name__ == "__main__":
    main()
