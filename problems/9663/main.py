# 9663. N-Queen

import sys
import time
from collections.abc import Callable
from typing import Any

Function = Callable[..., Any]
Vec2 = tuple[int, int]
input = sys.stdin.readline


def timer(fn: Function) -> Function:
    def decorator(*args, **kwargs) -> Any:
        elapsed = time.time()
        ret = fn(*args, **kwargs)
        elapsed = time.time() - elapsed
        print(f"Elapsed time: {elapsed:.3f}")
        return ret

    return decorator


def dead(q1: Vec2, q2: Vec2) -> bool:
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q2[0] - q1[0]) == abs(q2[1] - q1[1]):
        return True
    return False


# Passed only in pypy3
def n_queen(n: int, queens: list[int] = []) -> int:
    count = 0

    c = len(queens)
    for r in range(n):
        if r in queens:
            continue

        if any(c - qc == abs(r - qr) for qc, qr in enumerate(queens)):
            continue

        if c == n - 1:
            count += 1
        else:
            queens.append(r)
            count += n_queen(n, queens)
            queens.pop()

    return count


# Passed in pypy3 and python3
def bit_queen(n: int, strt: int = 0, left: int = 0, right: int = 0) -> int:
    bitmap = (1 << n) - 1
    if strt == bitmap:
        return 1

    count = 0
    nxtrt = bitmap & ~(strt | left | right)
    while nxtrt > 0:
        cur = nxtrt & -nxtrt
        count += bit_queen(n, strt | cur, (left | cur) << 1, (right | cur) >> 1)
        nxtrt -= cur

    return count


# @timer
def solve(n: int) -> int:
    return bit_queen(n)


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
