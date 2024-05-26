def main():
    wc, hc, ws, hs = map(int, input().split())
    print(int(wc-ws >= 2 and hc-hs >= 2))


if __name__ == '__main__':
    main()
