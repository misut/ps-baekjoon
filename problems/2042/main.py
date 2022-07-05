# 2042. 구간 합 구하기

import math
import sys
from array import array
from collections.abc import Callable, Sequence


class Segment:
    def __init__(self, key: Callable[[int, int], int], nums: Sequence[int]) -> None:
        self._key = key
        self._len = len(nums)

        self._lim = (1 << math.ceil(math.log2(len(nums)) + 1)) - 1
        self._arr = array("q", [0 for _ in range(self._lim)])
        self.setvals(nums)

    def __getitem__(self, interval: int | slice) -> int:
        if isinstance(interval, int):
            raise IndexError(
                "Segment doesn't support indexing by an integer. Use slice instead."
            )
        return self.getval(interval.start, interval.stop - 1)

    def __setitem__(self, idx: int, val: int) -> None:
        self.setval(idx, val)

    def getval(self, stt: int, fin: int) -> int:
        if stt == 0 and fin == self._len - 1:
            return self._arr[0]

        def _getval(idx: int, beg: int, end: int) -> int:
            if stt > end or fin < beg:
                return 0

            mid = (beg + end) // 2
            if stt <= beg and fin >= end:
                return self._arr[idx]

            l, r = _getval(idx * 2 + 1, beg, mid), _getval(idx * 2 + 2, mid + 1, end)
            return self._key(l, r)

        return _getval(0, 0, self._len - 1)

    def setvals(self, nums: Sequence[int]) -> None:
        def _setvals(idx: int, beg: int, end: int) -> int:
            if beg == end:
                self._arr[idx] = nums[beg]
                return self._arr[idx]

            mid = (beg + end) // 2

            l, r = _setvals(idx * 2 + 1, beg, mid), _setvals(idx * 2 + 2, mid + 1, end)
            self._arr[idx] = self._key(l, r)
            return self._arr[idx]

        _setvals(0, 0, self._len - 1)

    def setval(self, at: int, val: int) -> None:
        if at not in range(self._len):
            return 0

        def _setval(idx: int, beg: int, end: int) -> None:
            if beg > at or end < at:
                return self._arr[idx]

            if beg == end == at:
                self._arr[idx] = val
                return self._arr[idx]

            mid = (beg + end) // 2
            l, r = _setval(idx * 2 + 1, beg, mid), _setval(idx * 2 + 2, mid + 1, end)
            self._arr[idx] = self._key(l, r)
            return self._arr[idx]

        _setval(0, 0, self._len - 1)


if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().split())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]

    seg_sum = Segment(
        key=lambda a, b: a + b,
        nums=numbers,
    )
    for _ in range(m + k):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            seg_sum[b - 1] = c
        else:
            print(seg_sum[b - 1 : c])
