def main():
    from math import sqrt
    s1, s2, s3, s4 = map(int, input().split())
    semiperimeter = (s1 + s2 + s3 + s4) / 2
    print(sqrt(
        (semiperimeter - s1) *
        (semiperimeter - s2) *
        (semiperimeter - s3) *
        (semiperimeter - s4)
    ))


if __name__ == '__main__':
    main()
