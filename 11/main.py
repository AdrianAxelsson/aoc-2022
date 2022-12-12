def print_solution(day, p1, p2):
    print(f"** AoC 2022 - Day {day} Solution **")
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


class Monkey:
    def __init__(self, items, operation, test, actions):
        self.items = items
        self.operation = operation
        self.test = test
        self.actions = actions

    def get_item_list(self):
        return list(self.items)

    def get_test_divide_num(self):
        return int(self.test.split()[2])

    def inspect(self, item, divisor):
        old = int(item)
        new = 0
        operation = self.operation.split()
        if operation[2] == "old":
            test_num = old
        else:
            test_num = int(operation[2])
        match operation[1]:
            case "*":
                new = old * test_num
            case "+":
                new = old + test_num
        if divisor == 3:
            worry = new // divisor
        else:
            worry = new % divisor
        test = self.test.split()
        if worry % int(test[2]) == 0:
            return [int(self.actions[0].split()[-1]), worry]
        else:
            return [int(self.actions[1].split()[-1]), worry]


def throw_item(source, target, item):
    source.items.pop(0)
    target.items.append(item)


def get_common_divisor(monkeys):
    divisor = 1
    for monkey in monkeys:
        divisor *= monkey.get_test_divide_num()
    return divisor


def create_monkeys(monkey_inputs):
    monkeys = []
    for x in monkey_inputs:
        info = x.splitlines()
        items = info[1].split(":")[1].replace(" ", "").split(",")
        operation = info[2].split(":")[1].strip().split("=")[1].strip()
        test = info[3].split(":")[1].strip()
        actions = [info[4].split(":")[1].strip()]
        actions.append(info[5].split(":")[1].strip())
        monkeys.append(Monkey(items, operation, test, actions))
    return monkeys


def monkey_action(rounds, monkeys, p2=False):
    divisor = get_common_divisor(monkeys) if p2 else 3
    inspect_list = [0 for _ in range(len(monkeys))]
    for x in range(rounds):
        for i in range(len(monkeys)):
            for item in monkeys[i].get_item_list():
                result = monkeys[i].inspect(item, divisor)
                inspect_list[i] += 1
                throw_item(monkeys[i], monkeys[result[0]], result[1])
    inspect_list.sort(reverse=True)
    return inspect_list[0] * inspect_list[1]


def main():
    with open("input.lst") as f:
        input_monkeys = f.read().split("\n\n")

    p1 = monkey_action(20, create_monkeys(input_monkeys))
    p2 = monkey_action(10000, create_monkeys(input_monkeys), p2=True)
    print_solution(11, p1, p2)


if __name__ == "__main__":
    main()
