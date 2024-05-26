def main():
    n, m = map(int, input().split())
    forecast = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            result = 0
            if i - 1 >= 0:
                result += forecast[i][j] < forecast[i-1][j]
            if i + 1 < n:
                result += forecast[i][j] < forecast[i+1][j]
            if j - 1 >= 0:
                result += forecast[i][j] < forecast[i][j-1]
            if j + 1 < m:
                result += forecast[i][j] < forecast[i][j+1]
            if result == 4:
                print('Jebb')
                return
    print('Neibb')


if __name__ == '__main__':
    main()
