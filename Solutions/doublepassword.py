def main():
    pwd1 = [*input()]
    pwd2 = [*input()]
    print(2**sum([pwd1[x]!=pwd2[x] for x in range(4)]))


if __name__ == '__main__':
    main()
