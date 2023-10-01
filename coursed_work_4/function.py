from classes.get_from_hhru import Vacancy
from classes.get_from_superjob import VacancySuperJob
from classes.work_with_json import WorkWithJson

from classes.input_error import Input_error


def start_with_user():
    """Начало работы, приветствие и выбор сайта для поиска"""
    site = ["HeadHunter", "SuperJob", "Местная БД"]
    choоse_platforms = input("Здравствуйте, выберите сайт для поиска вакансий:\n"
                            f"1- {site[0]}\n"
                            f"2- {site[1]}\n"
                            f"3- {site[2]}\n"
                            "4- Выход\n")
    if choоse_platforms == "1":
        print(f"Выбранная платформа - {site[0]}")
        vacancies_from_hh = Vacancy()
        return vacancies_from_hh
    elif choоse_platforms == "2":
        print(f"Выбранная платформа - {site[1]}")
        superjob_api = VacancySuperJob()
        return superjob_api
    elif choоse_platforms == "3":
        print(f"Выбранная платформа - {site[2]}")
        file_json = WorkWithJson()
        return file_json.get_vacancies()
    elif choоse_platforms == "4":
        print("До свидания")
        return None
    else:
        raise Input_error


def find_vacancy():
    """Поиск вакансий по ключевому слову и отображение по указанному количеству"""
    vacancies_from = start_with_user()
    if vacancies_from is not None:
        search_query = input("Введите ключевое слово: ")
        vacancies_from.get_vacancies(search_query)
        if not vacancies_from.get_vacancies(search_query):
            print(f"Вакансий с {search_query}. не найдено")
            return
        filter_words = input("Введите критерий сортировки вакансий:\n"
                                 "'Название вакансии' -- 1 \n"
                                 "'Город' -- 2 \n")
        per_page = int(input("Введите количество вакансий для вывода: "))
        if isinstance(per_page, int):
            if filter_words == "1":
                print("Сортировка по названию:")
                return vacancies_from.sort_by('Название вакансии', per_page)
            elif filter_words == "2":
                print("Сортировка по городу")
                city = input("Введите название города: ")
                if vacancies_from.sort_by(city, per_page):
                    return vacancies_from.sort_by(city, per_page)
                else:
                    raise Input_error
            else:
                raise Input_error
        else:
            raise ValueError
    else:
        return None

def main():
    """Вывод найденных вакансий и дальнейшие действия с ними"""

    try:
        vacancy_sort = find_vacancy()
        if vacancy_sort is not None:
            print("Найденные вакансии:")
            for i in vacancy_sort:
                print(i)
            while True:
                next_move = int(input("Выберите дальнейшее действие: \n"
                                      "1 - добавление вакансии в json-файл\n"
                                      "2 - удаление вакансии из json-файла\n"
                                      "3 - получение информации о вакансии из файла\n"
                                      "4 - сравнение вакансий по заработной плате\n"
                                      "5 - выход\n"))

                if isinstance(next_move, int):
                    if next_move == 1:
                        add_vacancy(vacancy_sort)
                        continue
                    elif next_move == 2:
                        del_vacancy()
                        continue
                    elif next_move == 3:
                        print("Для получения информации о вакансии укажите её id : ")
                        full_info()
                        continue
                    elif next_move == 4:
                        print("Для сравнения вакансий по заработной плате введите id вакансий:")
                        comparison_by_salary()
                        continue
                    elif next_move == 5:
                        exit("До свидания")
                else:
                    raise Input_error
            return vacancy_sort
        else:
            return None
    except (Input_error, ValueError) as error:
        print(error.message)

# s = WorkWithJson()
# print(s.get_vacancy())

def add_vacancy(vacancies):
    """Добавление вакансии в файл"""
    from_vacancies = WorkWithJson()
    if vacancies is not None:
        add_vacancy = int(input(
            "Для добавления вакансии в файл введите 'id вакансии': "))
        vacancy_add_list = []
        if isinstance(add_vacancy, int):
            for i in vacancies:
                if i['id вакансии'] == add_vacancy:
                    vacancy_add = Vacancy(vacancy_id=i['id вакансии'],
                                          vacancy_name=i['Название'],
                                          vacancy_url=i['cсылка'],
                                          vacancy_salary=i['Заработная плата'],
                                          vacancy_city=i['Город'],
                                          vacancy_requirement=i['Требование'],
                                          vacancy_responsibility=i['Обязанности']
                                          )
                    vacancy_add_list.append(vacancy_add.to_dict())
            from_vacancies.add_vacancy(vacancy_add_list)
            print("Вакансия добавлена в файл!")
        else:
            raise ValueError


def del_vacancy():
    """Удаление вакансий из файла"""
    vacancies_from = WorkWithJson()
    delete_vacancy = int(input(
        "Для удаления вакансии из файла,укажите 'id вакансии': "))
    if isinstance(delete_vacancy, int):
        result = vacancies_from.delete_vacancy(delete_vacancy)
        return result
    else:
        raise ValueError


def full_info():
    """Получение информации о вакансии из файла"""
    vacancies_from = WorkWithJson()
    print(f"Список вакансий в местной БД:\n"
          f"{vacancies_from.get_vacancy()}")
    id_vacancy = int(input("id вакансии: "))
    if isinstance(id_vacancy, int):
        print(f"Информация о вакансии с id {id_vacancy}: ")
        vacancies_from.get_vacancies_by(id_vacancy)
    else:
        raise ValueError

def comparison_by_salary():
    """Сравнение двух добавленных в json вакансий по заработной плате"""
    vacancies_from = WorkWithJson()
    id_vac_x = int(input("Вакансия №1: "))
    id_vac_y = int(input("Вакансия №2: "))
    if isinstance(id_vac_x, int) and isinstance(id_vac_y, int):
        salary = vacancies_from.get_vacancies_by(id_vac_x, id_vac_y)
        vacancies_from.vacancy_salary = int(
            salary[0].split('-')[0]) if salary[0].split('-')[0].isdigit() else 0
        vacancies_from.other_salary = int(
            salary[1].split('-')[0]) if salary[1].split('-')[0].isdigit() else 0

        if vacancies_from.vacancy_salary >= vacancies_from.other_salary:
            print(f"Вакансия {id_vac_x} c заработной платой {vacancies_from.vacancy_salary},\n"
                  f"больше или равна вакансии {id_vac_y} c заработной платой {vacancies_from.other_salary}")
        else:
            print(f"Вакансия {id_vac_y} c заработной платой {vacancies_from.vacancy_salary},\n"
                  f"меньше или равна вакансии {id_vac_x} c заработной платой {vacancies_from.other_salary}")
    else:
        raise ValueError