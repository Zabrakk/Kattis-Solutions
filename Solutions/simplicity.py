def main():
    from sys import stdin
    for line in stdin:
        removed = 0
        chars = list(line.strip())
        while len((unique_chars:=set(chars))) > 2:
            c = sorted([(c, chars.count(c)) for c in unique_chars], key=lambda x: x[1])[0][0]
            while c in chars:
                chars.remove(c)
                removed += 1
        print(removed)


if __name__ == '__main__':
    main()
