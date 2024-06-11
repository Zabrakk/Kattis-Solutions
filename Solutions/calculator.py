def main():
    from sys import stdin
    for line in stdin:
        print(f'{eval(line):.2f}')


if __name__ == '__main__':
    main()
