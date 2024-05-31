def main():
    input()
    a, c = 0, 0
    for i in input():
        if c > 0 and i == '1':
            a += 1
            c = 2
        elif c > 0:
            a += 1
            c -= 1
        elif i == '1':
            a += 1
            c = 2
    print(a)


if __name__ == '__main__':
    main()
