def check(matr: list[str], x: int, y: int, i: int, j: int, word: str) -> bool:
    curr = 0
    while curr < len(word) and 0 <= x < len(matr) and 0 <= y < len(matr[0]):
        if word[curr] != matr[x][y]:
            break
        x += i
        y += j
        curr += 1
    return curr == len(word)


with open("input.txt") as f:
    lines = f.readlines()

res = sum(
    check(lines, x, y, i, j, "XMAS")
    for x in range(len(lines))
    for y in range(len(lines[0]))
    for i in range(-1, 2)
    for j in range(-1, 2)
    if i or j
)
print(res)
