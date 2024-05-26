def main():
    set_num = 1
    while (num_names := int(input())):
        names = sorted([input() for _ in range(num_names)], key=lambda x: len(x))
        print(f'SET {set_num}')
        set_num += 1
        for i in range(0, len(names), 2):
            print(names[i])
        names = list(reversed(names))
        for i in range(len(names)%2, len(names), 2):
            print(names[i])


if __name__ == '__main__':
    main()
