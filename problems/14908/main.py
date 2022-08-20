# 14908. 구두 수선공

import sys

Job = tuple[int, int]  # (day, charge)
input = sys.stdin.readline


def descending(a: Job, b: Job) -> bool:
    return a[1] * b[0] >= a[0] * b[1]


def solve(jobs: list[Job]) -> list[int]:
    sequence = []
    for idx, job in enumerate(jobs, 1):
        for sidx, job_idx in enumerate(sequence):
            if not descending(jobs[job_idx - 1], job):
                sequence.insert(sidx, idx)
                break
        else:
            sequence.append(idx)

    return sequence


if __name__ == "__main__":
    n = int(input())

    jobs = []
    for day in range(n):
        t, s = map(int, input().split())
        jobs.append((t, s))

    print(*solve(jobs))
