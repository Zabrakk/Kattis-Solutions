from math import gcd
from fractions import Fraction


def calc_gcd(a, b):
    greates_common_divisor = gcd(a, b)
    a = a // greates_common_divisor
    b = b // greates_common_divisor
    return a, b


def main():
    a, b = map(int, input().split('/'))
    a, b = calc_gcd(a, b)
    F = Fraction(a, b)
    C = F * Fraction(5, 9) - Fraction(160, 9)
    if C.denominator == 1:
        print(f'{C.numerator}/{C.denominator}')
    else:
        print(C)


if __name__ == '__main__':
    main()
