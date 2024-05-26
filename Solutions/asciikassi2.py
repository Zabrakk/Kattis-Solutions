def main():
    n = int(input())
    ctr = 1
    print(' '*(n+1) + 'x')
    for i in range(n, 0, -1):
        print(' '*i + '/' + ' '*ctr + '\\')
        ctr += 2
    print('x' + ' '*ctr + 'x')
    for i in range(1, n+1):
        ctr -= 2
        print(' '*i + '\\' + ' '*ctr + '/')
    print(' '*(n+1) + 'x')


if __name__ == '__main__':
    main()
