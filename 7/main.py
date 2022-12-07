from collections import defaultdict


def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def find_dirs_100000(file_system):
    size_sum = 0
    for dir in file_system:
        if file_system[dir] <= 100000:
            size_sum += file_system[dir]
        else:
            return size_sum
    return False


def find_dir_to_delete(file_system):
    free_space = 70000000 - file_system["//"]
    space_required = 30000000
    space_to_free = space_required - free_space
    for dir in file_system:
        if file_system[dir] >= space_to_free:
            dir_size = file_system[dir]
            return dir_size
    return False


def main():
    current_dir = []
    fs = defaultdict(int)

    with open("input.lst") as f:
        for line in f:
            line = line.strip()
            if line[0] == "$":
                if "cd" in line:
                    cd_path = line.split()[-1]
                    if cd_path == "..":
                        current_dir.pop()
                    else:
                        current_dir.append(cd_path + "/")
            elif line[0].isdigit():
                for i in range(len(current_dir)):
                    if i == 0:
                        fs[(''.join(current_dir))] += int(line.split()[0])
                    else:
                        fs[(''.join(current_dir[:-i]))] += int(line.split()[0])

    fs = dict(sorted(fs.items(), key=lambda x: x[1]))

    p1 = find_dirs_100000(fs)
    p2 = find_dir_to_delete(fs)

    print_solution(7, p1, p2)


if __name__ == "__main__":
    main()
