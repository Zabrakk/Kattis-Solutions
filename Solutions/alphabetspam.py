def main():
    whitespaces = 0
    lowercase = 0
    uppercase = 0
    symbols = 0
    S = input()
    n = len(S)

    for c in S:
        if c .islower():
            lowercase += 1
        elif c.isupper():
            uppercase += 1
        elif c == '_':
            whitespaces += 1
        else:
            symbols += 1
    print(whitespaces / n)
    print(lowercase / n)
    print(uppercase / n)
    print(symbols / n)


if __name__ == '__main__':
    main()
