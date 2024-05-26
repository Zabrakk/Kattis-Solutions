def main():
   inp = input().split('()')
   print('correct' if inp[0] == inp[1] else 'fix')


if __name__ == '__main__':
    main()
