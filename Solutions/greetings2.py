def main():
    inp = input().strip()
    print(inp[:inp.rindex('e')] + 'e'*inp.count('e') + inp[inp.rindex('e'):])


if __name__ == '__main__':
    main()
