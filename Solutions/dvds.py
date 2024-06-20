def main():
    for _ in range(int(input())):
        num_dvds = int(input())
        dvds = list(map(int, input().split()))
        val = 1

        for dvd_id in dvds:
            if dvd_id == val:
                val += 1
        print(num_dvds - val + 1)


if __name__ == '__main__':
    main()
