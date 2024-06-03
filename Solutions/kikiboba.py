def main():
    inp = input()
    b_count = inp.count('b')
    k_count = inp.count('k')

    if b_count > k_count:
        print('boba')
    elif k_count > b_count:
        print('kiki')
    elif b_count == 0 and k_count == 0:
        print('none')
    elif k_count == b_count:
        print('boki')


if __name__ == '__main__':
    main()
