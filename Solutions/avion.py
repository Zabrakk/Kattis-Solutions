def main():
    from sys import stdin
    a = ' '.join([str(i+1) for i, name in enumerate(stdin.readlines()) if 'FBI' in name])
    print(a if a else 'HE GOT AWAY!')


if __name__ == '__main__':
    main()
