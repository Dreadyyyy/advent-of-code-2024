from itertools import chain

with open("input.txt") as f:
    disk = f.readline().strip("\n")

fs = [
    [str(i // 2)] * int(c) if i % 2 == 0 else ["."] * int(c) for i, c in enumerate(disk)
]
fs = list(chain(*fs))

curr_pos = fs.index(".")
while curr_pos < len(fs):
    if fs[curr_pos] != ".":
        curr_pos += 1
        continue

    curr_c = fs.pop()
    while len(fs) > curr_pos and curr_c == ".":
        curr_c = fs.pop()

    if curr_pos == len(fs):
        break

    fs[curr_pos] = curr_c


res = sum(i * int(c) for i, c in enumerate(fs))
print(res)
