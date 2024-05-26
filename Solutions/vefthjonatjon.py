def main():
    from sys import stdin
    cpu, memory, hdd = 0, 0, 0
    for line in stdin.readlines()[1:]:
        if line[0] == 'J':
            cpu += 1
        if line[2] == 'J':
            memory += 1
        if line[4] == 'J':
            hdd += 1
    if cpu > 0 and memory > 0 and hdd > 0:
        print(min([cpu, memory, hdd]))
    else:
        print(0)


if __name__ == '__main__':
    main()
