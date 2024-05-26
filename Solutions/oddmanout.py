def main():
    from collections import Counter
    for case_num in range(int(input())):
        input()
        guest_nums = Counter(list(map(int, input().split())))
        print(f'Case #{case_num+1}: {guest_nums.most_common()[len(guest_nums) -1 ][0]}')


if __name__ == '__main__':
    main()