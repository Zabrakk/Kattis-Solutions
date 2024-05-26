def main():
    popularity = {}
    for _ in range(int(input())):
        s, a = input().split()
        if s not in popularity:
            popularity[s] = int(a)
        else:
            popularity[s] += int(a)
    print(sorted(popularity, key=lambda name: popularity[name], reverse=True)[0])


if __name__ == '__main__':
    main()
