# 4963. 섬의 개수

import sys
from itertools import product

Vec2 = tuple[int, int]
input = sys.stdin.readline


def surroundings(pos: Vec2) -> list[Vec2]:
    return [
        (pos[0] - 1, pos[1]),
        (pos[0] - 1, pos[1] - 1),
        (pos[0], pos[1] - 1),
        (pos[0] + 1, pos[1] - 1),
        (pos[0] + 1, pos[1]),
        (pos[0] + 1, pos[1] + 1),
        (pos[0], pos[1] + 1),
        (pos[0] - 1, pos[1] + 1),
    ]


def visit(islands: dict[Vec2, bool], pos: Vec2, visited: set[Vec2]) -> None:
    if not islands.get(pos, False):
        return

    visited.add(pos)
    for nxt in surroundings(pos):
        if nxt in visited:
            continue

        visit(islands, nxt, visited)


def solve(islands: dict[Vec2, bool], size: Vec2) -> int:
    answer = 0
    visited: set[Vec2] = set()
    for pos in product(range(size[0]), range(size[1])):
        if not islands.get(pos, False) or pos in visited:
            continue

        visit(islands, pos, visited)
        answer += 1

    return answer


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)

    islands = {}
    while True:
        islands.clear()
        r, c = map(int, input().split())
        if c == 0 and r == 0:
            break

        for col in range(c):
            for row, land in enumerate(map(int, input().split())):
                islands[(col, row)] = bool(land)

        print(solve(islands, (c, r)))
