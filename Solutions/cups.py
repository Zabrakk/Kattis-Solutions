def main():
    r = []
    for _ in range(int(input())):
        inp = input().split()
        if inp[0].isnumeric():
            inp = [inp[1], int(inp[0])//2]
        else:
            inp[1] = int(inp[1])
        r.append(inp)
    for e in sorted(r, key=lambda x:x[1]):
        print(e[0])


if __name__ == '__main__':
    main()
