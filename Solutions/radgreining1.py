def main():
    n, m = map(int, input().split())
    s = ['?'] * n
    for _ in range(m):
        position, section = input().split()
        position = int(position) - 1
        for c in section:
            if s[position] != '?' and s[position] != c:
                s = 'Villa'
                break
            s[position] = c
            position += 1
        if s == 'Villa':
            break
    print(''.join(s))


if __name__ == '__main__':
    main()
