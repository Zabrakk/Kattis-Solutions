LAYOUTS = [
    list("~1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./ "),
    list("~1234567890[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz "),
    list("0248613579=-/bjarkigust.,loempdcnvq;[]yzhwfx'~ ")
]
IDXS = {'qwerty': 0, 'dvorak': 1, 'bjarki': 2}


def main():
    user_layout, keyboard_layout = input().split(' on ')
    idx_user, idx_keyboard = IDXS[user_layout], IDXS[keyboard_layout]
    result = ''
    for c in input():
        if user_layout == keyboard_layout:
            result += c
        else:
            result += LAYOUTS[idx_keyboard][LAYOUTS[idx_user].index(c)]
    print(result)


if __name__ == '__main__':
    main()
