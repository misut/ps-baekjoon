# 2739. 구구단

if __name__ == "__main__":
    number = int(input())

    for multiplier in range(1, 10):
        print(f"{number} * {multiplier} = {number * multiplier}")
