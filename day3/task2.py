import re

with open("input.txt") as f:
    text = f.read()

delims = ["do()"] + re.findall(r"do\(\)|don't\(\)", text)
blocks = re.split(r"do\(\)|don't\(\)", text)
blocks = [b for i, b in enumerate(blocks) if delims[i] == "do()"]

command_blocks = [re.findall(r"mul\(\d{1,3},\d{1,3}\)", b) for b in blocks]
commands = [c for block in command_blocks for c in block]

res = sum(int(c[4 : (i := c.find(","))]) * int(c[i + 1 : -1]) for c in commands)
print(res)
