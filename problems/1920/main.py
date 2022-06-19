if __name__ == "__main__":
    N = int(input())
    A = {int(x): True for x in input().strip().split()}
    M = int(input())
    B = [int(x) for x in input().strip().split()]
    for n in B:
        if n in A:
            print(1)
        else:
            print(0)
