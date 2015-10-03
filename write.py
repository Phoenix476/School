import json


# def find_teacher(file_name, teacher, class_):
#     file = json.load(open(file_name, 'r'))
#     teacher = teacher.split(' ')
#     for line in file:
#         if file['name'] == teacher[0] and file['surname'] == teacher[1]:
#             file['class'] == class_


def save_data(file_name, dict_list):
    file = open(file_name, 'w')
    dict_list = json.dumps(dict_list, sort_keys=True, ensure_ascii=False, indent='')
    file.write(dict_list)
    file.close()


students = [{'name': 'Иван', 'surname': 'Иванов', 'middle_name': 'Иванович'}, {'name': 'Дмитрий', 'surname': 'Дмитриев', 'middle_name': 'Дмитриевич'}]
teachers = [{'name': 'Александр', 'surname': 'Пушкин', 'middle_name': 'Сергеевич', 'class': '5А'}, {'name': 'Фёдор', 'surname': 'Достоевский', 'middle_name': 'Михайлович', 'class': '6Б'}]

save_data('My_Students', students)
save_data('My_Teachers', teachers)

# teacher = 'Александр Пушкин'
# class_ = '5А'
# if find_teacher('My_Teachers', teacher):
#