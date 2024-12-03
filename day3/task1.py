import re

with open("input.txt") as f:
    r = r"mul\([0-9]+,[0-9]+\)"
    command_lines = [re.findall(r, l) for l in f.readlines()]

args = [c.replace("mul", "").strip("()").split(",") for l in command_lines for c in l]

res = sum(int(a1) * int(a2) for a1, a2 in args)
print(res)
