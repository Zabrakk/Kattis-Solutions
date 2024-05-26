def main():
    s = input()
    s2 = s[0]
    if len(s) == 1:
        print(s2)
        return
    for i in range(1, len(s)):
        if s[i-1] != s2[-1]:
            s2 += s[i-1]
    if s[-1] != s2[-1]:
        s2 += s[-1]
    print(s2)


if __name__ == '__main__':
    main()
