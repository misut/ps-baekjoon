# 1149. RGB거리

import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    prices = [0, 0, 0]
    for _ in range(n):
        current_prices = list(map(int, sys.stdin.readline().split()))
        current_prices[0] += min(prices[1], prices[2])
        current_prices[1] += min(prices[0], prices[2])
        current_prices[2] += min(prices[0], prices[1])
        prices = current_prices

    print(min(prices))
