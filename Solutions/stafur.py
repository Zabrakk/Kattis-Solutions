def main():
    c = input()
    if c == 'Y':
        print('Kannski')
    else:
        print('Jebb' if c in ['A','E','I','O','U'] else 'Neibb')


if __name__ == '__main__':
    main()
