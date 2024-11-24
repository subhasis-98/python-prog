mark = int(input("Enter the marks secured: "))

if mark >= 90 and mark <= 100:
    print("Grade O")
elif mark >= 80 and mark < 90:
    print("Grade A")
elif mark >= 70 and mark < 80:
    print("Grade B")
elif mark >= 60 and mark < 70:
    print("Grade C")
elif mark >= 50 and mark < 60:
    print("Grade D")
elif mark >= 40 and mark < 50:
    print("Grade E")
else:
    print("Fail")
