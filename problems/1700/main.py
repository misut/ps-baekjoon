# 1700. 멀티탭 스케줄링

import sys
from collections import Counter

input = sys.stdin.readline


def solve(appliances: list[int], consents: int) -> int:
    answer = 0
    counter = Counter(appliances)
    applied = []
    for cur, appliance in enumerate(appliances):
        counter[appliance] -= 1
        # 이미 꽂혀져 있으면 아무것도 하지 않음
        if appliance in applied:
            continue

        # 남는 콘센트 공간이 있으면 꽂음
        if len(applied) < consents:
            applied.append(appliance)
            continue

        min_app = min(applied, key=lambda app: counter[app])
        min_count = counter[min_app]
        if min_count == 0:
            # 더이상 필요없는 전기용품을 뽑음
            pull = min_app
        else:
            # 가장 나중에 필요한 전기용품을 뽑음
            pull = max(applied, key=lambda app: appliances[cur:].index(app))

        applied.remove(pull)
        applied.append(appliance)
        answer += 1

    return answer


if __name__ == "__main__":
    n, k = map(int, input().split())
    appliances = list(map(int, input().split()))
    print(solve(appliances, n))
