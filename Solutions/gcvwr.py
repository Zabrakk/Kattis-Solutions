def main():
    G, T, _ = map(int, input().split())
    print(int((G-T)*0.9-sum(map(int, input().split()))))


if __name__ == '__main__':
    main()
