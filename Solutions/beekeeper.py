def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    while (n:=int(input())) > 0:
        words = {input(): 0 for _ in range(n)}
        for word in words:
            for vowel in vowels:
                words[word] += word.count(vowel*2)
        print(sorted(words, key=lambda k: words[k])[-1])


if __name__ == '__main__':
    main()
