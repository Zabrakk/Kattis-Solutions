BINARY_FLIPS = [
    0b110_100_000, 0b111_010_000, 0b011_001_000,
    0b100_110_100, 0b010_111_010, 0b001_011_001,
    0b000_100_110, 0b000_010_111, 0b000_001_011
]


def read_expected_result_as_binary():
    result = ''.join([input() for _ in range(3)])
    result = ''.join([['0','1'][char == '*'] for char in list(result)])
    return int(result, 2)


def breadth_first_search(expected_result):
    Q = set([0])    # Create a queue
    seen = set()    # Create storage for seen nodes
    ctr = 0         # Result
    while expected_result not in Q:
        explore_next = set()    # Storage for nodes to which the current one leads to
        while Q:
            v = Q.pop()
            if v not in seen:
                for flip in BINARY_FLIPS:       # Perform all flips
                    explore_next.add(v ^ flip)  # Flip squares with the XOR operator
                seen.add(v)
        ctr += 1
        Q.update(explore_next)
    return ctr


def main():
    for _ in range(int(input())):
        expected_result = read_expected_result_as_binary()
        print(breadth_first_search(expected_result))


if __name__ == '__main__':
    main()
