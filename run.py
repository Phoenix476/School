# *********
# Задание
# *********
# Допишите код програмы в соответствии с примечаниями (TODO и FIXME) в коде программы
# Реализовать нужно только те пункты меню, о которых сказано в примечаниях
# Все неработающие пункты(если такие останутся) пометьте каким-нить символом(например *) и сделайте к ним заглушки
# TОDО-шки не удаляйте, а меняйте TODO --> TODO(complete)
# Меняйте структуру программы, если это нужно
# Дописывайте вспомогателные функции
# Постарайтесь убрать существующие дублирования кода(где это возможно) и избежать дальнейших повторений
# TODO* - наиболее сложные задачи

# *********
# Доп. Задания (для желающих и тех, у кого осталось время)
# *********
# 1. Напишите скрипт(программу), которая будет удалять всех учеников и учителей из файлов с данными, не имеющих
# отношения
# к текущей школе и текущим класса (указанным в school.json)
# 2. Сделайте функцию обертку, для удобного вывода цветного текста
# 3. Разукрасьте текст программы, сделав его удобнее для восприятия

import os
import json
from utilities import location, clear, get_full_name, search, get_people

school_data = []
students_data = []
teachers_data = []


# Функции


def edit_student():
    global students_data

    def student_delete():
        return

    menu = [
        {'text': 'Удалить ученика',
         'func': student_delete
         },
        {'text': 'Перевести в другой класс'}
    ]
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        for num, student in enumerate(students_data):
            print("%s) %s || %s" % (num + 1, get_full_name(student), student['class']))
        student_num = int(input('Укажите номер ученика(или НОЛЬ, для создания нового): '))
        if 0 < student_num <= len(students_data):
            student = students_data[student_num - 1]
            print("Вы выбрали %s " % get_full_name(student) + '||' + student['class'])
            loop
        else:
            print('Такого номера нет, введите другой номер')
    return


def class_delete():
    global school_data
    global teachers_data
    global students_data
    while True:
        print(school_data['classes'])
        class_room = input("Введите класс: ")
        if class_room in school_data["classes"]:
            # TODO(complete): 1. Удалить класс из school.json
            # write_school = json.dumps(school_data['classes'].remove(class_room),
            #                           sort_keys=True, ensure_ascii=False, indent='')
            pass
            # TODO: 2. Удалить класс у всех учителей
            # TODO: 3. Заменить класс у всех учеников на '' (считается что ученик ожидает перевод в новый класс)
            # TODO: 4. Не забыть обновить информацию в файлах
            # TODO: 5. Сделать изменения в меню 'MENU > Информация > Об учениках' (вывести учеников без классов)
            break
        else:
            print('Вы ввели несуществующий класс')
            # TODO: и предложить ввести класс повторно


def teachers():
    global teachers_data
    global school_data
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("     MENU > Информация > Об учителях")
    # TODO(complete): дописать вывод по аналогии с учениками
    for class_room in school_data["classes"]:
        print("Учителя '%s' класса: " % class_room)
        for num, teacher in enumerate(search(teachers_data, class_room=class_room)):
            print("     ", '%s)' % (num + 1), get_full_name(teacher))
            print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")
    return


def students():
    global students_data
    global school_data
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("     MENU > Информация > Об учениках")
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for num, student in enumerate(search(students_data, class_room=class_room)):
            # FIXME(complete): учесть(во всей программе), в файле могут быть ученики из других школ
            # TODO(complete): Добавить нумерацию учеников для каждого класса
            print("     ", '%s)' % (num + 1), get_full_name(student))
            print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")
    return


def classrooms():
    global teachers_data
    global students_data
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Информация > О классах")
        print("Все классы нашей школы")
        print("||", " || ".join(school_data['classes']), "||")
        print()
        class_room = input("Введите класс, для подробной информации по нему \n"
                           " (или Enter для возврата в предыдущее меню):")
        if class_room in school_data["classes"]:  # FIXME(complete): сообщить, если выбран несуществующий класс
            print("\nИнформация по %s классу:" % class_room)
            # TODO(complete): вывести всех учеников и учителей указанного класса
            id_students_in_class = get_people(students_data, class_room=class_room, school='%s %s' % school)
            id_teachers_in_class = get_people(teachers_data, class_room=class_room, school='%s %s' % school)
            print("     Учителя: %s" % ','.join(['%s %s %s' % (teacher['name'], teacher['middle_name'],
                                                               teacher['surname'])
                                                 for teacher in teachers_data
                                                 if teacher['id'] in id_teachers_in_class]))
            print("     Ученики: %s" % ','.join(['%s %s %s' % (student['name'], student['middle_name'],
                                                               student['surname'])
                                                 for student in students_data
                                                 if student['id'] in id_students_in_class]))
            input("Нажмите Enter для возврата в предыдущее меню")
            # TODO*: Сделать возврат в предыдущее меню(во всех местах программы).
            # TODO(complete):Выход из программы только по пункту "выйти"
            break
        else:
            print('Такого класса нет в школе')
    return


def loop(menu):
    while True:
        print("     MENU")
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        for num, el in enumerate(menu):
            print('%s. %s' % (num + 1, el['text']))
        choice = int(input(': '))
        if choice == len(menu):
            return
        menu_choice = menu[choice - 1]
        if menu_choice.get('func'):
            menu_choice['func']()
        if menu_choice.get('sub_menu'):
            loop(menu_choice['sub_menu'])


# Load data


def load_data():
    global school_data
    global students_data
    global teachers_data

    with open(location('data/school.json')) as f:
        school_data = json.load(f)

    with open(location('data/Students.json')) as f:
        students_data = json.load(f)

    with open(location('data/Teachers.json')) as f:
        teachers_data = json.load(f)


load_data()
# MAIN
school = (school_data['number'], 'школа')

clear()
# Про цветной текст ищите в гугле
print("\033[1;34m*\033[1;m" * 24)
print("\033[1;34m* Welcome to %s %s *\033[1;m" % (school_data['number'], school_data['type']))
print("\033[1;34m*\033[1;m" * 24)
menu = [
    {'text': 'Информация',
     'sub_menu':
         [
             {'text': 'О классах',
              'func': classrooms
              },
             {'text': 'Об учениках',
              'func': students
              },
             {'text': 'Об учителях',
              'func': teachers
              },
             {'text': 'Назад'
              }
         ]
     },
    {'text': 'Редактировать',
     'sub_menu':
         [{'text': 'Класс',
           'sub_menu': [
               {'text': 'Удалить существующий',
                'func': class_delete
                },
               {'text': 'Назад'
                }
           ]
           },
          {'text': 'Ученика',
           'func': edit_student
           },
          {'text': 'Учителя',
           'sub_menu': 1
           }

          ]},
    {'text': 'Выход'

     }
]
print("2. Редактировать")
print("3. Выйти")
loop(menu)
while True:
    if choice == '2':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Редактировать")
        print("1. Класс")
        print("2. Ученика")
        print("3. Учителя")
        choice = input(": ")
        while True:
            if choice == '2':
                clear()
                print("*" * 24)
                print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
                print("*" * 24)
                print("     MENU > Редактировать > Ученика")
                for num, student in enumerate(students_data):
                    print("%s) %s || %s" % (num, get_full_name(student), student['class']))
                student_num = input('Укажите номер ученика(или НОЛЬ, для создания нового): ')
                print()
                print("Вы выбрали %s " % 'unknown')  # TODO: Указать выбранного ученика и отобразить
                # по нему полную информацию
                # FIXME: не забыть обработать ввод номера несуществующего ученика
                print('1. Удалить ученика')
                print('2. Перевести в другой класс')
                print('3. Назад')
                # TODO: реализовать удаление и перевод ученика
                # TODO*: реализовать создание нового ученика с вводом всех необходимых параметров
                # TODO: не забыть, нельзя задать ученику несуществующий класс
            elif choice == '3':
                clear()
                print("*" * 24)
                print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
                print("*" * 24)
                print("     MENU > Редактировать > Учителя")
                # Заглушка
                print("Данный пункт находится в разработке")
                input("Нажмите Enter для возврата в предыдущее меню")
    else:
        print("Error: Not correct menu item")
        break
