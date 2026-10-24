# Write a Python program that accepts a student's name and marks in three subjects.

# Requirements:

# - Calculate total marks and average.
# - Use conditional statements to determine the grade.
# - Create a function to calculate the average and return the result.
# - Display the student's name, total marks, average, and grade.
# - Validate that marks are between 0 and 100.

student_name = input("Enter students name:")
Science_marks = float(input("Enter marks of student in Science:"))
English_marks = float(input("Enter marks of student in English:"))
Math_marks = float(input("Enter marks of student in Math:"))

Total_Marks = (Science_marks + English_marks + Math_marks)
average_marks = (Total_Marks)/3


def total_average(total):
    return total


if (Science_marks < 0 or Science_marks > 100 or
    English_marks < 0 or English_marks > 100 or
        Math_marks < 0 or Math_marks > 100):
    print("Invalid Marks, Enter marks between 0 and 100")

else:
    average = total_average(average_marks)

    if average >= 90:
        Grade = "A+"
    elif average >= 80:
        Grade = "A"
    elif average >= 70:
        Grade = "B+"
    elif average >= 60:
        Grade = "B"
    elif average >= 50:
        Grade = "C+"
    elif average >= 40:
        Grade = "C"
    else:
        Grade = "F"

print(f"Students Name: {student_name}")
print(f"Total Marks: {Total_Marks}")
print(f"Average: {average}")
print(f"Grade: {Grade}")