def main():
    import sys
    import math
    for l in sys.stdin:
        if l=='0 0 0\n':
            break
        r, m, c=map(float, l.split())
        print(math.pi*r*r,4*c/m*r*r)


if __name__ == '__main__':
    main()
