import sys

tile = [-1 for _ in range(2001)]
tile[0], tile[1], tile[2] = 0, 1, 2


def tiling(n):
    if n <= 0:
        return 0
    if tile[n] < 0:
        tile[n] = tiling(n - 1) + tiling(n - 2)
    return tile[n]


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    n = int(input())
    print(tiling(n) % 10007)
