def main():
    from sys import stdin
    vals = []
    for line in stdin:
        vals.append(int(line))
    print(sum(vals))


if __name__ == '__main__':
    main()
