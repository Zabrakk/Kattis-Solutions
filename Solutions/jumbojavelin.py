def main():
    import sys
    inp = sys.stdin.readlines()[1:]
    print(sum([int(val) for val in inp])-len(inp)+1)


if __name__ == '__main__':
    main()
