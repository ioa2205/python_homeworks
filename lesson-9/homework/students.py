import csv
from collections import defaultdict

data = [
    {'Name': 'Alice', 'Subject': 'Math', 'Grade': 85},
    {'Name': 'Bob', 'Subject': 'Science', 'Grade': 78},
    {'Name': 'Carol', 'Subject': 'Math', 'Grade': 92},
    {'Name': 'Dave', 'Subject': 'History', 'Grade': 74}
]

with open('grades.csv', mode='w', newline='') as csvfile:
    fieldnames = ['Name', 'Subject', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)

grades = []

with open('grades.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row['Grade'] = int(row['Grade'])
        grades.append(row)


subject_grades = defaultdict(list)

for entry in grades:
    subject = entry['Subject']
    grade = entry['Grade']
    subject_grades[subject].append(grade)

average_grade = []

for subject, marks in subject_grades.items():
    avg = sum(marks)/len(marks)
    average_grade.append({'Subject':subject, 'Average_grades':avg})


with open('average_grades.csv', mode='w', newline='') as file:
    fieldnames = ['Subject', 'Average_grades']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for row in average_grade:
        writer.writerow({'Subject':row['Subject'], 'Average_grades':row['Average_grades']})

