import json


def student_add(data_students):
    # Записывает студента в файл
    student = 'Иван Иванович Краснов,Максим Максимович Максим,Дима Дмитриевич Дмитриев,Денис Денисович Денисов'
    student = student.split(',')

    dict_student = {'name': student[0], 'surname': student[2], 'middle_name': student[1]}
    dict_student = json.dumps(dict_student, sort_keys=True, ensure_ascii=False, indent='')
    data_students.write(dict_student)


def teacher_add(data_teachers):
    # Записывает учителя в файл
    teacher = 'Максим Максимович Меньшиков'
    teacher = teacher.split(' ')
    class_teacher = '5А,11Б,7А'
    class_teacher = class_teacher.split(',')
    dict_teacher = {'name': teacher[0], 'surname': teacher[2], 'middle_name': teacher[1], 'class': class_teacher}
    dict_teacher = json.dumps(dict_teacher, sort_keys=True, ensure_ascii=False, indent='')
    data_teachers.write(dict_teacher)


data_teachers = open('My_Teachers', 'r')
data_students = open('My_Students', 'r')
print(data_teachers.read())
print(data_students.read())
data_teachers.close()
data_students.close()

data_teachers = open('My_Teachers', 'w')
data_students = open('My_Students', 'w')

student_add(data_students)
teacher_add(data_teachers)

