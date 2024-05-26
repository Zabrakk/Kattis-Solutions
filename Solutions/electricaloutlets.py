def main():
    for _ in range(int(input())):
        tc = list(map(int, input().split()))
        print(sum(tc[1:]) - tc[0] + 1)


if __name__ == '__main__':
    main()
