import json


def id_search(data, **kwargs):
    # Возвращает id по заданному параметру
    ids = []
    result = False
    if 'class_room' in kwargs.keys():   # Переименовывает ключ class_room на class
        kwargs['class'] = kwargs.pop('class_room')
    for dict_data in data:
        for key in kwargs.keys():
            if (kwargs[key] == dict_data[key]) or (kwargs[key] in dict_data[key]):
                result = True
            else:
                result = False
                break
        if result:
            ids.append(dict_data['id'])
    return ids


students = open('Students_id.json', 'r')
data_students = json.load(students)
teachers = open('Teachers_id.json', 'r')
data_teachers = json.load(teachers)

lst_student = []

# 4.2

student_ids = id_search(data_students, name='Александр', middle_name='Валерьевич')
for id in student_ids:
    for student in data_students:
        if student['id'] == id:
            lst_student.append('%s %s %s' % (student['name'], student['middle_name'], student['surname']))
print(lst_student)

teachers_class = id_search(data_teachers, class_room='7 В')
print(teachers_class)


