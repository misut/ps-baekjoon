# 1016. 제곱 ㄴㄴ 수

import math
import sys

input = sys.stdin.readline


def solve(beg: int, end: int) -> int:
    fin = math.ceil(math.sqrt(end + 1))
    sqs = [sqr * sqr for sqr in range(2, fin)]

    remain = [True for _ in range(beg, end + 1)]
    for div in sqs:
        stt = beg + (div - beg % div) if beg % div > 0 else beg
        for num in range(stt, end + 1, div):
            remain[num - beg] = False

    return remain.count(True)


if __name__ == "__main__":
    mininum, maximum = map(int, input().split())
    print(solve(mininum, maximum))
