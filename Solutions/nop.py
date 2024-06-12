def main():
    instruction = list(input())
    num_nops = 0
    i = 0
    while i < len(instruction):
        if instruction[i].isupper():
            diff = i % 4
            if diff != 0:
                num_nops += (4-diff)
                instruction = instruction[:i] + ['x']*(4-diff) + instruction[i:]
        i += 1
    print(num_nops)


if __name__ == '__main__':
    main()
