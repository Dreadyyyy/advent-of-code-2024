import re

with open("input.txt") as f:
    text = f.read()

delims = ["do()"] + re.findall(r"do\(\)|don't\(\)", text)
blocks = re.split(r"do\(\)|don't\(\)", text)
blocks = [b for i, b in enumerate(blocks) if delims[i] == "do()"]

command_blocks = [re.findall(r"mul\([0-9]+,[0-9]+\)", b) for b in blocks]
commands = [c for block in command_blocks for c in block]

args = [c.replace("mul", "").strip("()").split(",") for c in commands]

res = sum(int(a1) * int(a2) for a1, a2 in args)
print(res)
