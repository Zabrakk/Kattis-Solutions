def main():
    name = input()
    new_name = ''

    for i, chr in enumerate(name):
        if i == 0:
            new_name += chr
        elif name[i-1] != chr:
            new_name += chr
    print(new_name)


if __name__ == '__main__':
    main()
