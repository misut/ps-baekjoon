import math

if __name__ == "__main__":
    A, B, V = [int(x) for x in input().strip().split()]
    print(math.ceil((V - A) / (A - B)) + 1)
