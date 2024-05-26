def main():
    input();print(sum([abs(x) for x in map(int, input().split()) if x < 0]))


if __name__ == '__main__':
    main()
