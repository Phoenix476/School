import json


def students_add(data_students):
    # Записывает студентов в файл
    list_students = []
    while len(list_students) < 5:
        student = 'Иван Иванович Краснов'
        student = student.split(' ')
        dict_student = {'name': student[0], 'surname': student[2], 'middle_name': student[1]}
        list_students.append(dict_student)
    list_students = json.dumps(list_students, ensure_ascii=False)
    data_students.write(list_students)


def teachers_add(data_teachers):
    # Записывает учителей в файл
    list_teachers = []
    while len(list_teachers) < 3:
        teacher = 'Максим Максимович Меньшиков'
        teacher = teacher.split(' ')
        dict_teacher = {'name': teacher[0], 'surname': teacher[2], 'middle_name': teacher[1]}
        list_teachers.append(dict_teacher)
    list_teachers = json.dumps(list_teachers, ensure_ascii=False)
    data_teachers.write(list_teachers)

data_teachers = open('My_Teachers', 'w')
data_students = open('My_Students', 'w')

students_add(data_students)
teachers_add(data_teachers)
