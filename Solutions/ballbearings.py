from math import *

def main():
    n = int(input())
    while n:
        n -= 1
        D, d, s = map(float, input().split())
        print(
            int(pi / asin((d + s) / (D - d)))
        )


if __name__ == '__main__':
    main()
