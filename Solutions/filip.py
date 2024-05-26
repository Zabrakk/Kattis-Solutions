def main():
    inp = input().split()
    inp[0] = int(str(inp[0])[::-1])
    inp[1] = int(str(inp[1])[::-1])
    print(max(inp))


if __name__ == '__main__':
    main()
