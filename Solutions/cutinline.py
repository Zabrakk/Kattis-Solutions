def main():
    names = [input() for _ in range(int(input()))]
    actions = [input() for _ in range(int(input()))]

    for action in actions:
        if 'leave' in action:
            names.remove(action.split()[1])
        else:
            _, cut, got_cut = action.split()
            if cut in names:
                names.remove(cut)
            idx = names.index(got_cut)
            names = names[:idx] + [cut] + names[idx:]

    for name in names:
        print(name)


if __name__ == '__main__':
    main()
