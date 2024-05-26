def main():
    k = int(input().split()[1])
    idx = list(map(int, input().split())).index(k)
    if idx == 0:
        print('fyrst')
    elif idx == 1:
        print('naestfyrst')
    else:
        print(f'{idx+1} fyrst')


if __name__ == '__main__':
    main()
