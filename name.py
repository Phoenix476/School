import json


def find_teacher(teacher):
    teacher = teacher.split(' ')
    for teacher_line in teachers:
        a = 10

def name(data):
    lst_name = []
    for dict_data in data:
        lst_name.append(dict_data['name'])
    return lst_name


def class_room(data, student_class):
    lst_student = []
    for dict_data in data:
        if dict_data['class'] == student_class:
            lst_student.append(dict_data['name']+' '+dict_data['surname'])
    if len(lst_student) == 0:
        lst_student = 'Учеников в этом классе нет или такого класса не существует'
    return lst_student


def school(data):
    lst_school = []
    for dict_data in data:
        lst_school.append(dict_data['school'])
    lst_school = set(lst_school)
    return lst_school

students = open('Students.json', 'r')
teachers = open('Teachers.json', 'r')
data_teachers = json.load(teachers)
data_students = json.load(students)

lst_name_teachers = name(data_teachers)
lst_name_students = name(data_students)
print(lst_name_students)
print(lst_name_teachers)

student_class = '5 А'
lst_students_class = class_room(data_students, student_class)
print(lst_students_class)

schools = school(data_students)
print(schools)

teacher = 'Александр Сергеевич Чёрный'







