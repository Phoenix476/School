import json


def student_teacher(student, data_teachers, data_students):
    # Возвращает всех учителей заданного ученика
    teachers = []
    for line in data_students:
        if student == '%s %s' % (line['name'], line['surname']):
            class_student = line['class']
            for line2 in data_teachers:
                for class_teacher in line2['class']:
                    if class_teacher == class_student:
                        teachers.append('%s %s' % (line2['name'], line['surname']))
    return teachers


def teacher_student(teacher, data_teachers, data_students):
    # Возращает всех учеников заданного учителя.
    students = []
    for dict_el in data_teachers:
        if teacher == '%s %s' % (dict_el['name'], dict_el['surname']):
            classlist = dict_el['class']
            for class_student in classlist:
                for student in data_students:
                    if student['class'] == class_student:
                        students.append('%s %s' % (student['name'], student['surname']))
    teacher_print = 'Учитель: %s \n' % teacher
    return teacher_print, students


def name(data):
    # Возвращает все имена учеников, написанных в файле
    lst_name = []
    for dict_data in data:
        lst_name.append(dict_data['name'])
    return lst_name


def class_room(data, student_class):
    # Возвращает всех учеников заданного класса или сообщение о том, что такого класса нет.
    lst_student = []
    for dict_data in data:
        if dict_data['class'] == student_class:
            lst_student.append(dict_data['name']+' '+dict_data['surname'])
    if len(lst_student) == 0:
        lst_student = 'Учеников в этом классе нет или такого класса не существует'
    return lst_student


def school(data):
    # Возвращает все школы, записанные в файле
    lst_school = []
    for dict_data in data:
        lst_school.append(dict_data['school'])
    lst_school = set(lst_school)
    return lst_school


with open('data/Students.json', 'r') as students, open('data/Teachers.json', 'r') as teachers:
    data_teachers = json.load(teachers)
    data_students = json.load(students)

    lst_name_teachers = name(data_teachers)
    lst_name_students = name(data_students)

    print('1.1.1:', '\n')
    for el in lst_name_students:
        print(el)

    print('1.1.2:', '\n')
    for el in lst_name_teachers:
        print(el)

    student_class = '5 А'
    lst_students_class = class_room(data_students, student_class)
    print('1.1.3:', '\n')
    for el in lst_students_class:
        print(el)

    schools = school(data_students)
    print('1.1.4:', '\n')
    for el in schools:
        print(el)

    print('1.2.1:', '\n')
    teacher = 'Александр Черный'
    teacher_print, students_list = teacher_student(teacher, data_teachers, data_students)
    print(teacher_print)
    for el in students_list:
        print(el)

    print('1.2.2:', '\n')
    student = 'Иван Иванов'
    teachers_list = student_teacher(student, data_teachers, data_students)
    for el in teachers_list:
        print(el)
    pass






