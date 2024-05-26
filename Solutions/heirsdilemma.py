def main():
    start, end = map(int, input().split())
    combinations = [val for val in range(start, end+1) if '0' not in str(val) and len(set(str(val))) == 6 and (val % 2 == 0 or val % 3 == 0)]
    ctr = 0
    for val in combinations:
        str_val = str(val)
        if sum([val % int(n) for n in str_val]) == 0:
            ctr += 1
    print(ctr)


if __name__ == '__main__':
    main()
