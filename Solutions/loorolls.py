def main():
    l, n = map(int, input().split())
    k, remainder = 1, l % n
    while remainder != 0:
        k += 1
        n -= remainder
        remainder = l % n
    print(k)


if __name__ == '__main__':
    main()
