def main():
    info, remember = [], []
    for _ in range(int(input())):
        name, score, date = input().split()
        info += [[name, int(score), date]]
    for entry in info:
        if entry[1] >= max([i[1] for i in info if i[2] == entry[2]]):
            remember += [entry]
    print(len(remember))
    for entry in sorted(remember, key=lambda x: x[0]):
        print(entry[0])


if __name__ == '__main__':
    main()
