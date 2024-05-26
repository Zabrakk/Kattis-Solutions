def main():
    n, k = map(int, input().split())
    s = input().split()
    print(' '.join([s[i] for i in range(k-1, n, k)]))


if __name__ == '__main__':
    main()
