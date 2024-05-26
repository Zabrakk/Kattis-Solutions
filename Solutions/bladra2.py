def main():
    v, a, t = map(int, input().split())
    print(v*t + 1/2 * a * (t**2))


if __name__ == '__main__':
    main()
