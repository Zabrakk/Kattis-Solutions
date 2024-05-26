def main():
    input()
    print('no' if sum(map(int, input().split()))%3 else 'yes')


if __name__ == '__main__':
    main()
