from sys import stdin
import heapq
import time


def explore(lines, y, x):
    explore_next = []
    heapq.heappush(explore_next, (y, x))
    while explore_next:
        y, x = explore_next.pop()
        if 0 <= y < len(lines) and 0 <= x < len(lines[y]):
            if lines[y][x] != '#':
                lines[y][x] = '#'
                heapq.heappush(explore_next, (y-1, x))
                heapq.heappush(explore_next, (y, x-1))
                heapq.heappush(explore_next, (y, x+1))
                heapq.heappush(explore_next, (y+1, x))


def main():
    inp = stdin.readlines()
    l = 0
    case = 1
    while l < len(inp):
        m, n = [int(x) for x in inp[l].split()]
        l += 1
        lines = [list(line.strip()) for line in inp[l:l+m]]
        l += m
        ctr = 0
        for y in range(m):
            for x in range(n):
                if lines[y][x] == '-':
                    ctr += 1
                    lines[y][x] = '#'
                    explore(lines, y-1, x)
                    explore(lines, y, x-1)
                    explore(lines, y, x+1)
                    explore(lines, y+1, x)
        print(f'Case {case}: {ctr}')
        case += 1


if __name__ == '__main__':
     main()
