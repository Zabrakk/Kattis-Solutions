def main():
    import sys
    vals=[]
    for line in sys.stdin:
        vals.append(int(line))
    print(2022 + int(vals[0]/vals[1]))


if __name__ == '__main__':
    main()
