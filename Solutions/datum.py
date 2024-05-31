def main():
    import datetime as dt
    d, m = map(int, input().split())
    print(dt.date(2009,m,d).strftime('%A'))


if __name__ == '__main__':
    main()
