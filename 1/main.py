with open("input.lst") as f:
  input = f.read().splitlines()

def get_calories(input):
  calories = []
  cals = 0
  input = input
  for line in input:
    if line == "":
      calories.append(cals)
      cals = 0
      continue
    cals = cals + int(line)
  return calories

calories = get_calories(input)
calories.sort()

p1 = calories[-1:][0]
p2 = sum(calories[-3:])

print("** AoC 2022 - Day 1 Solution **")
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
