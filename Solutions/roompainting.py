def main():
    from sys import stdin
    n, m = map(int, next(stdin).split())
    sizes = sorted([int(next(stdin)) for _ in range(n)])
    needed_sizes = [int(next(stdin)) for _ in range(m)]

    sum_of_closest_sizes = 0
    for s in needed_sizes:
        for s2 in sizes:
            if s2 >= s:
                sum_of_closest_sizes += s2
                break
    print(sum_of_closest_sizes-sum(needed_sizes))


if __name__ == '__main__':
    main()