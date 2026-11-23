MAX_GRACE = 5

subjects = []

n = int(input("Enter number of subjects: "))

total_marks = 0
total_max_marks = 0
all_passed = True

for i in range(n):
    print("\nSubject", i + 1)

    name = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    pass_mark = int(input("Enter pass marks: "))
    obtained = int(input("Enter marks obtained: "))

    
    if maximum <= 0 or pass_mark < 0 or pass_mark > maximum:
        print("Invalid maximum or pass marks!")
        raise SystemExit

    if obtained < 0 or obtained > maximum:
        print("Invalid obtained marks!")
        raise SystemExit

    grace = 0
    final_marks = obtained

    
    if obtained < pass_mark:
        shortage = pass_mark - obtained

        if shortage <= MAX_GRACE:
            grace = shortage
            final_marks = min(
                obtained + grace, maximum
            )

    
    if final_marks >= pass_mark:
        result = "PASS"
    else:
        result = "FAIL"
        all_passed = False

    total_marks += final_marks
    total_max_marks += maximum

    subjects.append([
        name, obtained, grace, final_marks, result
    ])


percentage = (total_marks / total_max_marks) * 100


if not all_passed:
    classification = "FAIL"
elif percentage >= 75:
    classification = "DISTINCTION"
elif percentage >= 60:
    classification = "FIRST CLASS"
elif percentage >= 50:
    classification = "SECOND CLASS"
elif percentage >= 40:
    classification = "THIRD CLASS"
else:
    classification = "FAIL"

print("\n========== EXAMINATION RESULT ==========")

print("Subject\tObtained\tGrace\tFinal\tResult")

for s in subjects:
    print(
        s[0], "\t", s[1], "\t\t",
        s[2], "\t", s[3], "\t", s[4]
    )

print("----------------------------------------")
print("Total Marks:", total_marks, "/", total_max_marks)
print("Percentage: {:.2f}%".format(percentage))
print("Final Classification:", classification)

print("========================================")
