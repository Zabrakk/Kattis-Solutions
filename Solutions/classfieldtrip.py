def main():
    from sys import stdin
    lines = stdin.readlines()
    s = lines[0].strip() + lines[1].strip()
    print(''.join(sorted(s)))


if __name__ == '__main__':
    main()
