def main():
    from sys import stdin
    next(stdin)
    result = sum([1 for color in stdin if 'pink' in color.lower() or 'rose' in color.lower()])
    print(result if result > 0 else 'I must watch Star Wars with my daughter')


if __name__ == '__main__':
    main()
