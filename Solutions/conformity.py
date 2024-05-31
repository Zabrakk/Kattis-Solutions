def main():
    courses = {}
    for _ in range(int(input())):
        combination = str(sorted(map(int,input().split())))
        if combination in courses.keys():
            courses[combination] += 1
        else:
            courses[combination] = 1
    m = max(courses.values())
    print(m * list(courses.values()).count(m))


if __name__ == '__main__':
    main()
