def main():
    corn = list(map(int, input().split()))
    N, KWF = map(int, input().split())
    print(
        N * (sum([corn[i] * corn[i+1] for i in range(0, len(corn), 2)]) // 5) // KWF
    )


if __name__ == '__main__':
    main()
