def main():
    input()
    incorrect_list = list(map(int, input().split()))
    correct_list = sorted(incorrect_list)
    print(sum([a != b for (a,b) in zip(correct_list, incorrect_list)]))


if __name__ == '__main__':
    main()
