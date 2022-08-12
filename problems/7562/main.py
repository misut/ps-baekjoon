# 7562. 나이트의 이동

import sys
from collections import deque

Vec2 = tuple[int, int]
input = sys.stdin.readline


def move_knight(pos: Vec2, l: int) -> list[Vec2]:
    movs = [
        (pos[0] - 1, pos[1] + 2),
        (pos[0] - 2, pos[1] + 1),
        (pos[0] - 2, pos[1] - 1),
        (pos[0] - 1, pos[1] - 2),
        (pos[0] + 1, pos[1] - 2),
        (pos[0] + 2, pos[1] - 1),
        (pos[0] + 2, pos[1] + 1),
        (pos[0] + 1, pos[1] + 2),
    ]

    return [mov for mov in movs if 0 <= mov[0] < l and 0 <= mov[1] < l]


def solve(beg: Vec2, end: Vec2, l: int) -> int:
    if beg == end:
        return 0

    v1, v2 = {beg: 0}, {end: 0}
    q1, q2 = deque([beg]), deque([end])

    while len(q1) > 0 or len(q2) > 0:
        stt = q1.popleft()
        for mov in move_knight(stt, l):
            if mov in v1:
                continue
            if mov in v2:
                return v1[stt] + v2[mov] + 1

            v1[mov] = v1[stt] + 1
            q1.append(mov)

        fin = q2.popleft()
        for mov in move_knight(fin, l):
            if mov in v2:
                continue
            if mov in v1:
                return v1[mov] + v2[fin] + 1

            v2[mov] = v2[fin] + 1
            q2.append(mov)

    return -1


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        l = int(input())
        beg: Vec2 = tuple(map(int, input().split()))[:2]
        end: Vec2 = tuple(map(int, input().split()))[:2]
        print(solve(beg, end, l))
