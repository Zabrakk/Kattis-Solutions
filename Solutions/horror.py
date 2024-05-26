def main():
    from sys import stdin
    N, _, L = map(int, next(stdin).split())
    horror_movies = list(map(int, next(stdin).split()))
    horror_index = {id: 0 for id in horror_movies}
    similar = {i: [] for i in range(N)}

    for _ in range(L):
        a, b = map(int, next(stdin).split())
        similar[a] += [b]
        similar[b] += [a]

    for id in horror_movies:
        for id2 in similar[id]:
            if id2 not in horror_movies:
                horror_index[id2] = horror_index[id] + 1
                horror_movies += [id2]

    for i in range(N):
        if i not in horror_index:
            print(i)
            return

    max_score = max(horror_index.values())
    print(sorted([id for id in horror_index if horror_index[id]==max_score])[0])


if __name__ == '__main__':
    main()