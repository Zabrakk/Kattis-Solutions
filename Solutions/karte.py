def main():
    s = input()
    s = [s[i:i+3] for i in range(0, len(s), 3)]
    if len(set(s)) != len(s):
        print('GRESKA')
    else:
        print(*[13 - [c[0]for c in s].count(k) for k in list('PKHT')])


if __name__ == '__main__':
    main()
