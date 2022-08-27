# 17435. 합성함수와 쿼리

import sys

input = sys.stdin.readline


# 2 ** 18 == 262144
def sqfx(fx: list[int], m: int) -> list[list[int]]:
    squares = [[f] * 19 for f in fx]

    for exp in range(1, 19):
        for idx in range(1, m + 1):
            squares[idx][exp] = squares[squares[idx][exp - 1]][exp - 1]

    return squares


def solve(n: int, x: int, sqrs: list[list[int]]) -> int:
    exp = 0
    while n > 0:
        if n & 1:
            x = sqrs[x][exp]

        exp += 1
        n >>= 1

    return x


if __name__ == "__main__":
    m = int(input())
    fx = [0] + list(map(int, input().split()))
    sqrs = sqfx(fx, m)

    q = int(input())
    for _ in range(q):
        n, x = map(int, input().split())
        print(solve(n, x, sqrs))
