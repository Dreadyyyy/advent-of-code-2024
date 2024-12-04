def check(matr: list[str], x: int, y: int, word: str) -> bool:
    if x + len(word) - 1 >= len(matr) or y + len(word) - 1 >= len(matr[0]):
        return False

    d1 = "".join([matr[x + i][y + i] for i in range(len(word))])
    d2 = "".join([matr[x + i][y + len(word) - 1 - i] for i in range(len(word))])

    return d1 in (word, word[::-1]) and d2 in (word, word[::-1])


with open("input.txt") as f:
    lines = f.readlines()

res = sum(
    check(lines, x, y, "MAS") for x in range(len(lines)) for y in range(len(lines[0]))
)
print(res)
