def main():
    from sys import stdin
    a, b, a_b = list(map(int, stdin.readlines()[1:]))
    if a > b or a_b == 0:
        print('VEIT EKKI')
    elif a-b  == a_b:
        print('JEDI')
    else:
        print('SITH')


if __name__ == '__main__':
    main()
