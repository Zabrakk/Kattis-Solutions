def main():
    _, T = map(int, input().split())
    x = list(map(int, input().split()))

    ctr, s = 0, 0
    for val in x:
        s += val
        if s > T:
            break
        ctr += 1
    print(ctr)


if __name__ == '__main__':
    main()
