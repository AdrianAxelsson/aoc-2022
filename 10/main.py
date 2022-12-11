def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def print_pixel(cycle, x, line_list):
    sprite_pos = [x-1, x, x+1]
    if cycle <= 40:
        if (cycle - 1) in sprite_pos:
            line_list[0].append("#")
        else:
            line_list[0].append(".")
    elif cycle <= 80:
        if (cycle - 41) in sprite_pos:
            line_list[1].append("#")
        else:
            line_list[1].append(".")
    elif cycle <= 120:
        if (cycle - 81) in sprite_pos:
            line_list[2].append("#")
        else:
            line_list[2].append(".")
    elif cycle <= 160:
        if (cycle - 121) in sprite_pos:
            line_list[3].append("#")
        else:
            line_list[3].append(".")
    elif cycle <= 200:
        if (cycle - 161) in sprite_pos:
            line_list[4].append("#")
        else:
            line_list[4].append(".")
    elif cycle <= 240:
        if (cycle - 201) in sprite_pos:
            line_list[5].append("#")
        else:
            line_list[5].append(".")


def check_signal(cycle, x, signal_map):
    for key in signal_map:
        if cycle == key:
            signal_map[key] = key * x


def main():
    cycle = 1
    x = 1
    instructions = []
    line_list = [[] for _ in range(6)]
    signal_map = {
        20: 0,
        60: 0,
        100: 0,
        140: 0,
        180: 0,
        220: 0
    }

    with open("input.lst") as f:
        for line in f:
            line = line.strip()
            if len(instructions) > 0:
                check_signal(cycle, x, signal_map)
                print_pixel(cycle, x, line_list)
                x += instructions.pop()
                cycle += 1
            if line == "noop":
                check_signal(cycle, x, signal_map)
                print_pixel(cycle, x, line_list)
                cycle += 1
                continue
            instructions.insert(0, int(line.split()[1]))
            check_signal(cycle, x, signal_map)
            print_pixel(cycle, x, line_list)
            cycle += 1

    p1 = sum(signal_map.values())
    p2 = "\n"
    for i in range(len(line_list)):
        p2 += ''.join(line_list[i]) + "\n"
    print_solution(10, p1, p2)


if __name__ == "__main__":
    main()
