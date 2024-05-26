def main():
    gifts = [input().split() for _ in range(int(input()))]
    print(sorted(gifts, key=lambda x: int(x[1]), reverse=True)[0][0])


if __name__ == '__main__':
    main()
