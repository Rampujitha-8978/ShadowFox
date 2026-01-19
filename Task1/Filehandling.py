import csv
import os

students = []

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Open file in read mode and create dictionary
file_path = os.path.join(script_dir, "student_marks.csv")
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

# 2. Add total_marks and average to dictionary
for student in students:
    marks = []
    for key in student:
        if key != "Name":
            marks.append(int(student[key]))

    total = sum(marks)
    average = total / len(marks)

    student["Total_Marks"] = total
    student["Average"] = round(average, 2)

# 3. Create new CSV file with updated data
output_file_path = os.path.join(script_dir, "student_marks_updated.csv")
with open(output_file_path, "w", newline="") as file:
    fieldnames = students[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("New file 'student_marks_updated.csv' created successfully.")
