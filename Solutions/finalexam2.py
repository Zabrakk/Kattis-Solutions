def main():
    s = 0
    n = int(input())
    inp = [input() for _ in range(n)]
    for i in range(1, n):
        if inp[i-1] == inp[i]:
            s += 1
    print(s)


if __name__ == '__main__':
    main()
