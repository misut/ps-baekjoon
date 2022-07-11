# 6549. 히스토그램에서 가장 큰 직사각형

import sys
from collections import deque
from dataclasses import dataclass

input = sys.stdin.readline


@dataclass
class Height:
    __slots__ = ["idx", "height"]

    idx: int
    height: int

    def area(self, at: int) -> int:
        return (at - self.idx) * self.height


def solve(heights: list[int]) -> int:
    ans = 0

    stk: deque[Height] = deque(maxlen=len(heights))
    for idx, height in enumerate(heights):
        at = idx
        while len(stk) > 0 and stk[-1].height > height:
            h = stk.pop()
            at = h.idx
            ans = max(ans, h.area(idx))

        stk.append(Height(at, height))
    else:
        idx += 1
        for h in stk:
            ans = max(ans, h.area(idx))

    return ans


if __name__ == "__main__":
    while True:
        n = list(map(int, input().split()))
        n, h = n[0], n[1:]

        if n == 0:
            break

        print(solve(h))
