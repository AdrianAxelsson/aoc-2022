import copy


def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


def get_stack_row(line):
    stack_row = []
    for row in line.split("\n"):
        for i in range(1, len(row), 4):
            stack_row.append(row[i])
    return stack_row


def get_instuction(line):
    instruction = list(''.join(c for c in line if c.isdigit()))
    if len(instruction) > 3:
        instruction[0] += instruction.pop(1)
    return instruction


def format_stack_dict(stack_rows):
    stacks_dict = {}
    stack_rows.reverse()
    for row in stack_rows[0]:
        stacks_dict[row] = []

    for row in stack_rows[1:]:
        for i in range(len(row)):
            if row[i] == " ":
                continue
            stacks_dict[str(i+1)].append(row[i])
    return stacks_dict


def move_stack(stacks_dict, instructions):
    for inst in instructions:
        for i in range(int(inst[0])):
            stacks_dict[inst[2]].append(stacks_dict[inst[1]].pop())


def move_stack_9001(stacks_dict, instructions):
    for inst in instructions:
        temp_list = []
        for i in range(int(inst[0])):
            temp_list.append(stacks_dict[inst[1]].pop())
        temp_list.reverse()
        for x in temp_list:
            stacks_dict[inst[2]].append(x)


def main():
    instruction_part = False
    move_instructions = []
    stack_rows = []
    with open("input.lst") as f:
        for line in f:
            line = line.splitlines()[0]
            if line == '':
                instruction_part = True
                continue
            if not instruction_part:
                stack_rows.append(get_stack_row(line))
            if instruction_part:
                move_instructions.append(get_instuction(line))

    stacks_dict = format_stack_dict(stack_rows)
    stacks_dict_2 = copy.deepcopy(stacks_dict)

    move_stack(stacks_dict, move_instructions)
    move_stack_9001(stacks_dict_2, move_instructions)

    p1 = ""
    p2 = ""
    for stacks in stacks_dict:
        p1 += (stacks_dict[stacks][-1:][0])
        p2 += (stacks_dict_2[stacks][-1:][0])

    print_solution(5, p1, p2)


if __name__ == "__main__":
    main()
