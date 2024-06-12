def main():
    l = int(input())
    num = int(input())
    multiple_found = False
    for _ in range(l - 1):
        if multiple_found:
            multiple_found = False
            num = int(input())
        else:
            n = int(input())
            if n % num == 0:
                print(n)
                multiple_found = True


if __name__ == '__main__':
    main()
