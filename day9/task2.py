with open("input.txt") as file:
    disk = file.readline().strip("\n")

files, free = [], []
pos = 0
for i, c in enumerate(disk):
    if i % 2 == 0:
        files.append((pos, int(c), i // 2))
    else:
        free.append((pos, int(c)))

    pos += int(c)

res = sum(
    digit * (start * 2 + length - 1) * length // 2 for start, length, digit in files
)

for i, (start, length, digit) in list(enumerate(files))[::-1]:
    for j, (start_free, length_free) in enumerate(free):
        if start_free > start:
            break

        if length_free < length:
            continue

        prev = (start * 2 + length - 1) * length // 2
        curr = (start_free * 2 + length - 1) * length // 2
        res -= digit * (prev - curr)

        free[j] = (start_free + length, length_free - length)
        break

print(res)
