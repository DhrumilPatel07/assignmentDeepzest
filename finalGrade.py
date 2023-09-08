Maths = float(input("Enter marks for Maths: "))
Chemistry = float(input("Enter marks for Chemistry: "))
Physics = float(input("Enter marks for Physics: "))
Biology = float(input("Enter marks for Biology: "))

average_marks = (Maths + Chemistry + Physics + Biology) / 4
passing_grade = 35

if average_marks >= passing_grade:
    result = "Pass"
else:
    result = "Fail"

print(f"Average Marks: {average_marks}")
print(f"Result: {result}")

