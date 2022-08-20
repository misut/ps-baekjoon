# 11066. 파일 합치기

import sys

MAX_COST = 50000000
input = sys.stdin.readline


def solve(chapters: list[int], k: int) -> int:
    accum = [0]
    for chapter in chapters:
        accum.append(accum[-1] + chapter)

    costs = [[-1 for _ in range(k + 1)] for __ in range(k + 1)]

    def merge(beg: int, end: int) -> int:
        if beg == end:
            return chapters[beg]

        if costs[beg][end] > 0:
            return costs[beg][end]

        costs[beg][end] = MAX_COST
        partial = accum[end + 1] - accum[beg]
        for idx in range(beg, end):
            costs[beg][end] = min(
                costs[beg][end],
                merge(beg, idx) + merge(idx + 1, end) + partial,
            )

        return costs[beg][end]

    return min(merge(0, idx) + merge(idx + 1, k - 1) for idx in range(k))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        chapters = list(map(int, input().split()))
        print(solve(chapters, k))
