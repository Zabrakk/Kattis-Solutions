def main():
    a, b, c = map(int, input().split())
    print(['wrong!', 'correct!'][a + b == c])


if __name__ == '__main__':
    main()
