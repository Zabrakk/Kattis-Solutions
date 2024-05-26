def main():
    for _ in range(int(input())):
        n = int(input())
        locations = sorted(map(int, input().split()))
        print(sum([locations[i+1]-locations[i] for i in range(n-1)])*2)


if __name__ == '__main__':
    main()
