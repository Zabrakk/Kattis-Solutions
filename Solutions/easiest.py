def sum_of_digits(n):
    return sum(map(int,list(str(n))))


def main():
    while (N:=int(input())) > 0:
        p = 11
        s_N = sum_of_digits(N)
        while 1:
            s = sum_of_digits(p*N)
            if s == s_N:
                print(p)
                break
            p += 1


if __name__ == '__main__':
    main()
