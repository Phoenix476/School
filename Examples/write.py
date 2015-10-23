import json


def get_index(data, surname):
    for teacher in data:
        if teacher['surname'] == surname:
            return data.index(teacher)


def save_data(file_name, dict_list):
    with open(file_name, 'w') as file:
        dict_list = json.dumps(dict_list, sort_keys=True, ensure_ascii=False, indent='')
        file.write(dict_list)
        pass


students = [{'name': 'Иван',
             'surname': 'Иванов',
             'middle_name': 'Иванович'},
            {'name': 'Дмитрий',
             'surname': 'Дмитриев',
             'middle_name': 'Дмитриевич',
             'class': '10Б'},
            {'name': 'Максим',
             'surname': 'Максимов',
             'middle_name': 'Максимович',
             'class': '8А'},
            {'name': 'Денис',
             'surname': 'Денисов',
             'middle_name': 'Денисьевич',
             'class': '10Б'}]
teachers = [{'name': 'Александр',
             'surname': 'Ядров',
             'middle_name': 'Сергеевич',
             'class': ['6Д'],
             'school': '16'},
            {'name': 'Александр',
             'surname': 'Пушкин',
             'middle_name': 'Сергеевич',
             'class': ['6Д'],
             'school': '12'},
            {'name': 'Фёдор',
             'surname': 'Достоевский',
             'middle_name': 'Михайлович',
             'class': ['10Б', '11А'],
             'school': '15'},
            {'name': 'Денис',
             'surname': 'Михалыч',
             'middle_name': 'Михайлович',
             'class': ['7А', '5В'],
             'school': '16'}]
surname_teacher = 'Пушкин'
surname_student = 'Иванов'
surname_teacher_delete = 'Михалыч'
surname_delete_class = 'Достоевский'
new_class = '5A'
student_class = '10Б'
school = '16'

# 3
teachers[get_index(teachers, surname_teacher)]['class'].append(new_class)
# 4
students.pop(get_index(students, surname_student))
# 6
teachers.pop(get_index(teachers, surname_teacher_delete))
# 8
teachers[get_index(teachers, surname_delete_class)]['class'].remove(student_class)

# 5
students = [student for student in students if student['class'] != student_class]

# 7
teachers = [teacher for teacher in teachers if teacher['school'] != school]

# 1
save_data('data/My_Students', students)
# 2
save_data('data/My_Teachers', teachers)



