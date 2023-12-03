import json


def load_students():
    '''
    возвращает список студентов
    :return:
    '''
    with open('students.txt') as file:
        students_json = file.read()
        students = json.loads(students_json)
        return students


def load_professions():
    '''
    возвращат список профессий
    :return:
    '''
    with open('professions.txt') as file:
        professions_json = file.read()
        professions = json.loads(professions_json)
        return professions


def get_student_by_pk(students, pk):
    '''
    Возвращает данные о
    студенте по его номеру
    :param students:
    :param pk:
    :return:
    '''
    for student in students:
        if student['pk'] == pk:
            return student['skills']
    else:
        return None


def get_profession_by_title(professions, title):
    '''
    Возвращает информацию о необходимых
    навыках для выбранной профессии
    :param professions:
    :param title:
    :return:
    '''
    for profession in professions:
        if profession['title'] == title:
            return profession['skills']
    else:
        return None


def check_fitness(student, profession):
    '''
    Возвращает словарь с
    данными о соответствии
    студента и професии
    :param student:
    :param profession:
    :return:
    '''
    has = set(profession) & set(student)
    lacks = set(profession) - set(student)
    fit_percent = len(has) / len(profession) * 100
    fitness = {}
    fitness['has'] = has
    fitness['lacks'] = lacks
    fitness['fit_percent'] = fit_percent
    return fitness

