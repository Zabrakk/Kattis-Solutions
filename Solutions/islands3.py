def breadth_first_search(img, r, c):
    Q = set()
    island_counter = 0
    for i in range(r):
        for j in range(c):
            if img[i][j] == 'L':
                island_counter += 1
                Q.add((i, j))
                while Q:
                    y, x = Q.pop()
                    if img[y][x] == 'L' or img[y][x] == 'C':
                        img[y][x] = 'W'
                        for y, x in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
                            if 0 <= y < r and 0 <= x < c:
                                Q.add((y, x))
    return island_counter


def main():
    r, c = map(int, input().split())
    img = [list(input()) for _ in range(r)]
    print(breadth_first_search(img, r, c))

if __name__ == '__main__':
    main()
