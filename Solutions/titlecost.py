def main():
    name, cost = input().split()
    if len(name) > float(cost):
        print(cost)
    else:
        print(len(name))


if __name__ == '__main__':
    main()
