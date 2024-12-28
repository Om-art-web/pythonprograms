#    Marks checking

marks = int(input("Enter marks between 0 and 100\n"))

if marks < 0 or marks > 100:
    print("Error")
elif marks < 40:
    print("Fail")
elif marks < 50:
    print("3rd Div")
elif marks < 60:
    print("2nd Div")
else:
    print("1st Div")

print(marks)
