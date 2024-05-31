def main():
    input()
    s = 0
    for val in map(int, input().split()):
        if val < 0:
            s += 1
    print(s)


if __name__ == '__main__':
    main()
