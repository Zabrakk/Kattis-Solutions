def main():
    date = list(map(int, input().split('/')))
    if date[0] <= 12 and date[1] <= 12:
        print('either')
    elif date[0] > 12:
        print('EU')
    else:
        print('US')


if __name__ == '__main__':
    main()
