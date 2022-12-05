import string


def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def generate_prio_map():
    prio_map = {}
    i = 1
    for c in string.ascii_letters:
        prio_map[c] = i
        i += 1
    return prio_map


def compare_compartments(sack):
    duplicates = set()
    for x in sack[0]:
        if x in sack[1]:
            duplicates.add(x)
    return duplicates


def get_item_prio(items, prio_map):
    prio = 0
    for item in items:
        prio += prio_map[item]
    return prio


def identify_badge(elf_group):
    e1, e2, e3 = elf_group
    badge = set()
    for x in e1:
        if x in e2:
            if x in e3:
                badge.add(x)
                break
    return badge


def main():
    prio_map = generate_prio_map()
    total_prio = 0
    total_badge_prio = 0
    elf_group = []

    with open("input.lst") as f:
        for line in f:
            line = line.splitlines()[0]
            # Part 1
            line_split = len(line) // 2
            sack = []
            sack.append(line[:line_split])
            sack.append(line[line_split:])
            item_duplicates = compare_compartments(sack)
            sack_item_prio = get_item_prio(item_duplicates, prio_map)
            total_prio += sack_item_prio
            # Part 2
            elf_group.append(line)
            if len(elf_group) == 3:
                badge = identify_badge(elf_group)
                elf_group = []
                badge_prio = get_item_prio(badge, prio_map)
                total_badge_prio += badge_prio

    print_solution(3, total_prio, total_badge_prio)


if __name__ == "__main__":
    main()
