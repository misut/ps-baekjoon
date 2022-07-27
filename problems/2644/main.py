# 2644. 촌수계산

import sys

input = sys.stdin.readline


def solve(parent: list[int], beg: int, end: int) -> int:
    chon = [-1 for _ in range(101)]

    stt, fin = beg, end
    chon[stt], chon[fin] = 0, 0
    while parent[stt] > 0 or parent[fin] > 0:
        if parent[stt] > 0:
            if chon[parent[stt]] < 0:
                chon[parent[stt]] = chon[stt] + 1
            else:
                return chon[parent[stt]] + chon[stt] + 1

            stt = parent[stt]

        if parent[fin] > 0:
            if chon[parent[fin]] < 0:
                chon[parent[fin]] = chon[fin] + 1
            else:
                return chon[parent[fin]] + chon[fin] + 1

            fin = parent[fin]

    return -1


if __name__ == "__main__":
    n = int(input())
    beg, end = map(int, input().split())

    m = int(input())
    parent = [0 for _ in range(101)]
    for _ in range(m):
        x, y = map(int, input().split())
        parent[y] = x

    print(solve(parent, beg, end))
