# 1655. 가운데를 말해요

import heapq
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())

    say = int(input())
    lhalf, rhalf = [], [say]
    print(rhalf[0])
    for count in range(1, n):
        say = int(input())
        if say < rhalf[0]:
            if len(rhalf) - len(lhalf) == 1:
                mov = heapq.heappushpop(lhalf, -say)
                heapq.heappush(rhalf, -mov)
            else:
                heapq.heappush(lhalf, -say)
        else:
            if len(rhalf) - len(lhalf) == 2:
                mov = heapq.heappushpop(rhalf, say)
                heapq.heappush(lhalf, -mov)
            else:
                heapq.heappush(rhalf, say)

        print(rhalf[0])
