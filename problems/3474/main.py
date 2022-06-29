# 3474. 교수가 된 현우

import sys


def solve(n: int) -> int:
    ans = 0
    while n >= 5:
        n //= 5
        ans += n

    return ans


if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        print(solve(int(sys.stdin.readline())))
