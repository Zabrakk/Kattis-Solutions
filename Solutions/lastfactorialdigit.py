def main():
    from sys import stdin
    from math import factorial
    print(*(f'{factorial(int(val))}'[-1] for val in stdin.readlines()[1:]), sep='\n')


if __name__ == '__main__':
    main()
