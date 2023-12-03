from functions import load_students
from functions import load_professions
from functions import get_student_by_pk
from functions import get_profession_by_title
from functions import check_fitness


def main():
    student_pk = int(input('Введите номер студента: \n'))
    if get_student_by_pk(load_students(), student_pk):
        student_name = load_students()[student_pk - 1]['full_name']
        print(f"Студент {student_name}")
        print(f"Знает {', '.join(get_student_by_pk(load_students(), student_pk))}")
    else:
        print('У нас нет такого студента.')
        quit()
    profession_title = input(f"Выберите специальность для оценки студента {student_name}: \n").title()
    if get_profession_by_title(load_professions(), profession_title):
        prof = check_fitness(get_student_by_pk(load_students(), student_pk),
                             get_profession_by_title(load_professions(), profession_title))
        print(f"Пригодность составляет: {round(prof['fit_percent'])}%")
        print(f"{student_name} знает {', '.join(prof['has'])}")
        print(f"{student_name} не знает {', '.join(prof['lacks'])}")
    else:
        print('У нас нет такой специальности.')
        quit()


if __name__ == '__main__':
    main()
