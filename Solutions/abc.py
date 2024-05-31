def main():
    numbers = sorted(map(int, input().split()))
    result = ''
    for c in input():
        if c == 'A':
            result += f'{numbers[0]} '
        elif c=='B':
            result += f'{numbers[1]} '
        else:
            result += f'{numbers[2]} '
    print(result)


if __name__ == '__main__':
    main()
