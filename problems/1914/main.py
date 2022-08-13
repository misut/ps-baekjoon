# 1914. 하노이 탑

import sys

Vec2 = tuple[int, int]
input = sys.stdin.readline


def hanoi(n: int, beg: int, mid: int, end: int) -> list[Vec2]:
    if n == 1:
        return [(beg, end)]

    return hanoi(n - 1, beg, end, mid) + [(beg, end)] + hanoi(n - 1, mid, beg, end)


def hanoi_brief(n: int) -> int:
    if n == 1:
        return 1

    return 2 * hanoi_brief(n - 1) + 1


def solve(n: int) -> None:
    if n <= 20:
        movs = hanoi(n, 1, 2, 3)
        print(len(movs))
        for mov in movs:
            print(*mov)
    else:
        print(hanoi_brief(n))


if __name__ == "__main__":
    n = int(input())
    solve(n)
