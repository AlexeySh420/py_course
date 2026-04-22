def main():

    school_class = { }

    while True:
        student_name = input("Enter student's name: ")
        if student_name == '':
            break
        student_score = int(input("Enter student's score: "))
        if student_score not in range(0, 10):
            break
        if student_name in school_class:
            school_class[student_name] += (student_score,)
        else:
            school_class[student_name] = (student_score,)
    for name in sorted(school_class.keys()):
        adding = 0
        counter = 0
        for score in school_class[name]:
            adding +=score
            counter += 1
        print(name, ":", adding / counter)

if __name__ == '__main__':
    main()