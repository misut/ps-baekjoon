# 2206. 벽 부수고 이동하기

import sys
from array import array
from collections import deque

Vec2 = tuple[int, int]

input = sys.stdin.readline


class Mat:
    __slots__ = ("_mat", "_size")

    def __init__(self, size: Vec2) -> None:
        self._mat = array("l", [0 for _ in range(size[0] * size[1])])
        self._size = size

    def __getitem__(self, pos: Vec2) -> int:
        return self._mat[pos[0] * self._size[1] + pos[1]]

    def __setitem__(self, pos: Vec2, val: int) -> None:
        self._mat[pos[0] * self._size[1] + pos[1]] = val


def connected(pos: Vec2, size: Vec2) -> list[Vec2]:
    con = [
        (pos[0] - 1, pos[1]),
        (pos[0] + 1, pos[1]),
        (pos[0], pos[1] - 1),
        (pos[0], pos[1] + 1),
    ]

    return [pos for pos in con if 0 <= pos[0] < size[0] and 0 <= pos[1] < size[1]]


def solve(mat: Mat) -> int:
    q: deque[tuple[Vec2, bool]] = deque([((0, 0), False)], maxlen=1000000)
    size = mat._size
    visited: dict[bool, Mat] = {
        False: Mat(size),
        True: Mat(size),
    }

    dest = (size[0] - 1, size[1] - 1)
    visited[False][(0, 0)] = 1
    while q:
        pos, broken = q.popleft()
        if pos == dest:
            return visited[broken][pos]

        for con in connected(pos, size):
            if visited[broken][con]:
                continue

            if mat[con]:
                if broken:
                    continue

                q.append((con, True))
                visited[True][con] = visited[broken][pos] + 1
                continue

            q.append((con, broken))
            visited[broken][con] = visited[broken][pos] + 1

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())

    mat = Mat(size=(n, m))
    for col in range(n):
        line = input().strip()
        for row, ch in enumerate(line):
            pos = (col, row)
            mat[pos] = int(ch)

    print(solve(mat))
