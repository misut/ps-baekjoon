# 5430. AC

import sys

input = sys.stdin.readline


def interpret(p: str, n: int, x: list[int]) -> str:
    beg, end = 0, n
    reverse = False
    for fn in p:
        if fn == "R":
            reverse = not reverse
            continue

        if reverse:
            end -= 1
        else:
            beg += 1

        if beg > end:
            return "error"

    ans = x[beg:end]
    if reverse:
        ans.reverse()

    return str(ans).replace(" ", "")


def solve(p: str, n: int, x: list[int]) -> None:
    print(interpret(p, n, x))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        p = input().strip()
        n = int(input())
        x = eval(input())
        solve(p, n, x)
