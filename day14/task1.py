from itertools import accumulate
import operator
from typing import Self, final


height, width, seconds = 103, 101, 100


@final
class Robot:
    def __init__(self, position: tuple[int, int], velocity: tuple[int, int]) -> None:
        self.position = position
        self.velocity = velocity

    def move(self, seconds: int) -> Self:
        x, y = self.position
        vx, vy = self.velocity

        self.position = (x + vx * seconds) % width, (y + vy * seconds) % height

        return self

    def quadrant(self) -> int | None:
        x, y = self.position

        if x == width // 2 or y == height // 2:
            return None

        return (x > width // 2) + (y > height // 2) * 2


with open("input.txt") as f:
    robots = [l.split(" ") for l in f.readlines()]

robots = [(p[2:].split(","), v[2:].split(",")) for p, v in robots]
robots = [(map(int, p), map(int, v)) for p, v in robots]
robots = [Robot((px, py), (vx, vy)) for (px, py), (vx, vy) in robots]

quadrants = [0] * 4
for i in filter(lambda x: x is not None, [r.move(seconds).quadrant() for r in robots]):
    quadrants[i] += 1

res = list(accumulate(quadrants, operator.mul))[-1]
print(res)
