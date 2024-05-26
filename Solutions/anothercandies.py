def main():
    for _ in range(int(input())):
        input()
        N = int(input())
        s = sum([int(input()) for _ in range(N)])
        print('NO' if s % N else 'YES')


if __name__ == '__main__':
    main()
