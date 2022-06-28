# 2357. 최솟값과 최댓값

import math
import sys
from array import array
from collections.abc import Callable


class Segment:
    __slots__ = ["_key", "_size", "_tree"]

    def __init__(self, key: Callable[[int, int], int], lst: list[int]) -> None:
        self.init(key=key, lst=lst)

    def init(self, key: Callable[[int, int], int], lst: list[int]) -> None:
        self._key: Callable[[int, int], int] = (
            lambda a, b: key(a, b) if a and b else a or b
        )
        self._size = len(lst)

        tree_size = 1 << math.ceil(math.log2(len(lst)) + 1)
        self._tree = array("l", [0 for _ in range(tree_size)])

        def segment(idx: int, beg: int, end: int) -> int:
            if beg == end:
                self._tree[idx] = lst[beg]
                return self._tree[idx]

            mid = (beg + end) // 2

            l, r = segment(idx * 2, beg, mid), segment(idx * 2 + 1, mid + 1, end)
            self._tree[idx] = self._key(l, r)
            return self._tree[idx]

        segment(1, 0, len(lst) - 1)

    def optimum(self, beg: int, end: int) -> int | None:
        def find(idx: int, stt: int, fin: int) -> int | None:
            if stt > end or fin < beg:
                return None

            mid = (stt + fin) // 2
            if beg <= stt and fin <= end:
                return self._tree[idx]

            l, r = find(idx * 2, stt, mid), find(idx * 2 + 1, mid + 1, fin)
            return self._key(l, r)

        return find(1, 0, self._size - 1)


if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    numbers = [int(sys.stdin.readline()) for _ in range(n)]

    seg_min = Segment(
        key=lambda a, b: a if a < b else b,
        lst=numbers,
    )
    seg_max = Segment(
        key=lambda a, b: a if a > b else b,
        lst=numbers,
    )
    for _ in range(m):
        beg, end = map(lambda n: int(n) - 1, sys.stdin.readline().split())
        print(seg_min.optimum(beg, end), seg_max.optimum(beg, end))
