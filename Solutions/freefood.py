def main():
    r = []
    for i in range(int(input())):
        start, end = map(int, input().split())
        r += list(range(start,end+1))
    print(len(set(r)))


if __name__ == '__main__':
    main()
