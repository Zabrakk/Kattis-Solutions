def main():
    n, k = map(int, input().split())
    s = 0
    for _ in range(k):
        s += int(input())
    print( (s-3*(n-k))/n, (s+3*(n-k))/n)


if __name__ == '__main__':
    main()
