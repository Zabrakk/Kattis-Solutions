def main():
    from sys import stdin, stdout
    while True:
        N, M  = map(int, next(stdin).split())
        if N == 0:
            return
        calls = [[(call:=list(map(int, next(stdin).split())))[2], call[2]+call[3]] for _ in range(N)]
        for _ in range(M):
            start, duration = map(int, next(stdin).split())
            stdout.write(
                f'{sum([call[0] < start + duration and start < call[1] for call in calls])}\n'
            )

if __name__ == '__main__':
    main()
