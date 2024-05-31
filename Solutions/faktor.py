def main():
    from math import ceil
    A, I = list(map(int, input().split()))

    for i in range(A*(I-1), A*(I+1)):
        if ceil(i/A) == I:
            print(i)
            break


if __name__ == '__main__':
    main()
