def main():
    from sys import stdin
    info = stdin.readlines()
    cost = float(info[0])

    s = 0
    for entry in info[2:]:
        w, l = entry.split()
        s += cost * float(w) * float(l)
    print(s)


if __name__ == '__main__':
    main()
