def main():
    X = int(input())
    counter = 1
    factor = 2
    while factor ** 2 <= X:
        if X % factor == 0:
            X //= factor
            counter += 1
        else:
            factor += 1
    print(counter)


if __name__ == '__main__':
    main()
