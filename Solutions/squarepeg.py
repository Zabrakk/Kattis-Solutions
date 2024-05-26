def main():
    L, R = map(int, input().split())
    print('fits' if L<R*(2**0.5) else 'nope')


if __name__ == '__main__':
    main()
