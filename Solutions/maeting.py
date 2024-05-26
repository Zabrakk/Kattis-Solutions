def main():
    students = {input(): 0 for _ in range(int(input()))}
    classes = [input().split() for _ in range(int(input()))]

    for c in classes:
        num_students = int(c[0])
        if num_students:
            for i in range(1, num_students+1):
                students[c[i]] += 1

    for student in sorted(students.items(), key=lambda x: x[1], reverse=1):
        print(student[1], student[0])


if __name__ == '__main__':
    main()
