with open("input.txt") as f:
    mp = [list(l.strip("\n")) for l in f.readlines()]

x, y = 0, 0
for r, l in enumerate(mp):
    if "^" in l and (c := l.index("^")) != -1:
        x, y = r, c

i, j = -1, 0
while 0 <= x < len(mp) and 0 <= y < len(mp[0]):
    if mp[x][y] != "#":
        mp[x][y] = "X"
        x, y = x + i, y + j
        continue

    x, y = x - i, y - j
    i, j = j, -i
    x, y = x + i, y + j

res = sum(c == "X" for l in mp for c in l)
print(res)
