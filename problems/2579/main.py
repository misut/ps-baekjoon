# 2579. 계단 오르기

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    prev = 0
    stairs = [0 for _ in range(300)]
    for idx in range(n):
        stair = int(input())
        stairs[idx] = stair + max(stairs[idx - 2], prev + stairs[idx - 3])
        prev = stair

    print(stairs[n - 1])
