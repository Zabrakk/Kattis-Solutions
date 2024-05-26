def main():
    from sys import stdin, stdout
    for T in range(int(next(stdin))):
        num_snappers, snaps = map(int, next(stdin).split())
        is_on = True
        for _ in range(0, num_snappers):
            if snaps % 2 == 0:
                is_on = False
                break
            snaps //= 2
        stdout.write(f'Case #{T+1}: {["OFF", "ON"][is_on]}\n')


if __name__ == '__main__':
    main()
