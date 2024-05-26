def main():
    inp = input()
    a_score, b_score = 0, 0
    tied = False
    for i in range(0, len(inp), 2):
        if inp[i] == 'A':
            a_score += int(inp[i+1])
        else:
            b_score += int(inp[i+1])
        if a_score == 10 and b_score == 10:
            tied = True
    if a_score >= 11 and not tied:
        print('A')
    elif b_score >= 11 and not tied:
        print('B')
    elif tied and a_score - b_score >= 2:
        print('A')
    elif tied and b_score - a_score >= 2:
        print('B')


if __name__ == '__main__':
    main()
