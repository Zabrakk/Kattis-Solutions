def main():
    dictionary = []
    while (word := input()) != '#':
        dictionary += [word]
    dictionary.sort(key=len)

    while (message := input()) != '#':
        while message[-1] != '|':
            message += input()
        message = message[:-1]
        dict_words_in_msg = [word for word in dictionary if word in message]
        words_start_and_end = []

        for word in dict_words_in_msg:
            i = 0
            while (i:=message.find(word, i)) != -1:
                words_start_and_end += [[i, i+len(word)-1]]
                i += len(word)
        words_start_and_end.sort(key=lambda x: x[1])

        prev_end = -1
        num_found_substrings = 0
        for entry in words_start_and_end:
            if entry[0] > prev_end:
                prev_end = entry[1]
                num_found_substrings += 1
        print(num_found_substrings)


if __name__ == '__main__':
    main()
