from typing import final


height, width = 103, 101


@final
class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]) -> None:
        self.position = position
        self.velocity = velocity

    def move(self, seconds: int) -> None:
        x, y = self.position
        vx, vy = self.velocity

        self.position = (x + vx * seconds) % width, (y + vy * seconds) % height


with open("input.txt") as f:
    robots = [l.split(" ") for l in f.readlines()]

robots = [(p[2:].split(","), v[2:].split(",")) for p, v in robots]
robots = [(map(int, p), map(int, v)) for p, v in robots]
robots = [Robot((px, py), (vx, vy)) for (px, py), (vx, vy) in robots]

mp = [["." for _ in range(width)] for _ in range(height)]
for i in range(10000):
    for r in robots:
        r.move(1)

    for x, y in [r.position for r in robots]:
        mp[y][x] = "*"

    if any("*" * 10 in "".join(l) for l in mp):
        print(i + 1)
        exit(0)

    mp = [["." for _ in range(width)] for _ in range(height)]
