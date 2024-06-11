def main():
    from collections import Counter
    input()
    freqs = map(int, input().split())
    counts = Counter(freqs)
    r = ''
    for entry in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        v, c = entry
        r += ' '.join([f'{v}' for _ in range(c)])
        r += ' '
    print(r[:-1])


if __name__ == '__main__':
    main()
