def main():
    from sys import stdin, stdout
    dir_flights = []
    for i, line in enumerate(stdin.readlines()[1:]):
        for j, val in enumerate(line.split()):
            if val != '-1':
                dir_flights.append(f'{i+1} {j+1} {val}\n')
    print(len(dir_flights))
    for entry in dir_flights:
        stdout.write(entry)

if __name__ == '__main__':
    main()
