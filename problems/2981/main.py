# 2981. 검문

import math
import sys

input = sys.stdin.readline


def solve(numbers: list[int], n: int) -> list[int]:
    ns = sorted(numbers)
    for idx in range(1, n):
        ns[idx] -= ns[0]

    mul = math.gcd(*ns[1:])
    mods = {mul}
    for mod in range(2, math.isqrt(mul) + 1):
        if mul % mod != 0:
            continue

        mods.add(mod)
        mods.add(mul // mod)

    mods = sorted(mods)
    if 1 in mods:
        mods.remove(1)
    return mods


if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    print(*solve(numbers, n))
