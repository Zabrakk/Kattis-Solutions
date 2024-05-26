def main():
    y = int(input())
    if y < 2021:
        print(1000)
    else:
        print(1000 + 100*(y-2020))


if __name__ == '__main__':
    main()
