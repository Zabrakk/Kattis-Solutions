def main():
    a, b = input(), input()
    print(sum([a[i] != b[i] for i in range(len(a))]) + 1)


if __name__ == '__main__':
    main()
