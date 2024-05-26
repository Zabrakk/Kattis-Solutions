def remove_ad(page, i, j, H, W):
    u_y, l_y, l_x, r_x = None, None, None, None
    for y in range(i, -1, -1):
        if page[y][j] == '+':
            u_y = y
            break

    for y in range(i, H):
        if page[y][j] == '+':
            l_y = y
            break

    for x in range(j, -1, -1):
        if page[i][x] == '+':
            l_x = x
            break

    for x in range(j, W):
        if page[i][x] == '+':
            r_x = x
            break

    if u_y is None or l_y is None or l_x is None or r_x is None:
        return

    furthest = (i-u_y, l_y-i, j-l_x, r_x-j).index(max(i-u_y, l_y-i, j-l_x, r_x-j))
    if furthest == 0:   # Upper Y
        for x in range(j, -1, -1):
            if page[u_y][x] != '+':
                break
            l_x = x
        for x in range(j, W):
            if page[u_y][x] != '+':
                break
            r_x = x
        for y in range(i, H):
            if page[y][l_x] != '+':
                break
            l_y = y
    elif furthest == 1: # Lower Y
        for x in range(j, -1, -1):
            if page[l_y][x] != '+':
                break
            l_x = x
        for x in range(j, W):
            if page[l_y][x] != '+':
                break
            r_x = x
        for y in range(i, -1, -1):
            if page[y][r_x] != '+':
                break
            u_y = y
    elif furthest == 2: # Left x
        for y in range(i, -1, -1):
            if page[y][l_x] != '+':
                break
            u_y = y
        for y in range(i, H):
            if page[y][l_x] != '+':
                break
            l_y = y
    else:               # Right x
        for y in range(i, -1, -1):
            if page[y][r_x] != '+':
                break
            u_y = y
        for y in range(i, H):
            if page[y][r_x] != '+':
                break
            l_y = y

    if set(page[u_y][l_x:r_x+1]) != {'+'}:
        return
    if set(page[l_y][l_x:r_x+1]) != {'+'}:
        return
    if set([page[y][l_x] for y in range(u_y, l_y+1)]) != {'+'}:
        return
    if set([page[y][r_x] for y in range(u_y, l_y+1)]) != {'+'}:
        return

    for y in range(u_y, l_y+1):
        for x in range(l_x, r_x+1):
            page[y][x] = ' '


def main():
    H, W = map(int, input().split())
    page = [list(input()) for _ in range(H)]
    ALLOWED_CHARACTERS = ['?', '!', ',', '.', ' ', '+']

    for i, row in enumerate(page):
        for j, c in enumerate(row):
            if not c.isalnum() and c not in ALLOWED_CHARACTERS:
                remove_ad(page, i, j, H, W)

    for row in page:
        print(''.join(row))


if __name__ == '__main__':
    main()
