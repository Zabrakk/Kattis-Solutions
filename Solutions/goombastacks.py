def main():
    from sys import stdin
    s = 0
    stdin.readline()
    for line in stdin:
        g, b = map(int, line.split())
        if g+s >= b:
            s += g
        else:
            print('impossible')
            return
    print('possible')


if __name__ == '__main__':
    main()
