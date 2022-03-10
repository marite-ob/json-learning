import json

file = open("students.json")
data = json.load(file)

for student in data["Students"]:
    print(student["FirstName"])

count = 0
total_age = 0
for student in data['Students']:
    count += 1
    total_age += int(student['Age'])

print(f'Avarage age: {total_age/ count}')

count_group_1 = 0
count_group_2 = 0
count_group_3 = 0

total_grade_group_1 = 0
total_grade_group_2 = 0
total_grade_group_3 = 0

for student in data['Students']:
    if int(student['Age']) < 20:
        count_group_1 += 1
        total_grade_group_1 += int(student['Grade'])
    elif int(student['Age']) < 30:
        count_group_2 += 1
        total_grade_group_2 += int(student['Grade'])
    else:
        count_group_3 =+ 1
        total_grade_group_3 += int(student['Grade'])

print(f'Avarage grade Age<20: {total_grade_group_1/count_group_1}')
print(f'Avarage grade 20<Age<30: {total_grade_group_2/count_group_2}')
print(f'Avarage grade Age>30: {total_grade_group_3/count_group_3}')

count_female = 0
count_male = 0

total_age_female = 0
total_grade_female = 0
total_age_male = 0
total_grade_male = 0

for student in data['Students']:
    if student['Gender'] == ['Famale']:
        count_female += 1
        total_age_female += int(student['Age'])
        total_grade_female  += int(student['Grade'])
    elif student['Gender'] == ['Male']:
        count_male += 1
        total_age_male += int(student['Age'])
        total_grade_male  += int(student['Grade'])

