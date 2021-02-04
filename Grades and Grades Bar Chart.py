#Grades and Grades chart

grades = []
numberOfGrades = int(input('How many grades do you want to enter? '))

for i in range(numberOfGrades):
    grade = input('Enter a grade: ')
    grades.append(grade)

for grade in grades:
    bar_chart = int(grade) * 'i'
    print(bar_chart, grade)
