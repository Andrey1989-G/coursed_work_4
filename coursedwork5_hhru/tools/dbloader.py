# добавляет данные в БД
import psycopg2
from services.get_from_hhru import HeadHunterAPI
from services.input_error import Input_error
from password import password

class DBLoader(HeadHunterAPI, Input_error):
    """обработка, загрузка данных в БД"""

    def __init__(self, vacancy_id=None, vacancy_name=None, vacancy_url=None,
                 vacancy_salary=None, vacancy_city=None, vacancy_requirement=None,
                 vacancy_responsibility=None, employer_name=None, employer_id = None):
        try:
            self.vacancy_id = vacancy_id
            self.vacancy_name = vacancy_name
            self.vacancy_url = vacancy_url
            self.vacancy_salary = vacancy_salary
            self.vacancy_city = vacancy_city
            self.vacancy_requirement = vacancy_requirement
            self.vacancy_responsibility = vacancy_responsibility
            self.employer_name = employer_name
            self.employer_id = employer_id
        except Input_error as s:
            print(s.message)

    def data_preparation_and_load_in_db(self, downloades_data):
        # Подключение к db
        conn = psycopg2.connect(
            host="localhost",
            database="db_hh_ru",
            user="postgres",
            password=password
        )
        try:
            with conn:
                with conn.cursor() as cur:
                    for item in downloades_data['items']:
                        salary = item['salary']
                        salary_range = f"{salary['from']}-{salary['to']}, валюта {salary['currency']}" if salary and salary[
                            'from'] and salary['to'] else "Не указано"
                        vacancy = []
                        res = {
                            "id вакансии": int(item['id']),
                            "Название вакансии": item['name'],
                            "Заработная плата": salary_range,
                            "Город": item["area"]["name"],
                            "Требование": item['snippet']['requirement'],
                            "Обязанности": item['snippet']['responsibility'],
                            "cсылка": item['url'],
                            "id работодателя": int(item["employer"]["id"]),
                            "название работодателя": item["employer"]["name"]
                        }

                        vacancy.append(res)
                        print(vacancy)
                    # заполнение таблицы vacancies
                        cur.execute(
                            "INSERT INTO vacancies (id_vacancies, name_vacancies,"
                            "salary, city, requirement, responsibility, url)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (vacancy[0]["id вакансии"],
                             vacancy[0]["Название вакансии"],
                             vacancy[0]["Заработная плата"],
                             vacancy[0]["Город"],
                             vacancy[0]["Требование"],
                             vacancy[0]["Обязанности"],
                             vacancy[0]["cсылка"])
                            )
                    # заполнение таблицы corporations
                        cur.execute(
                            "INSERT INTO corporations (id_employer, id_vacancies, name_employer)"
                            "VALUES (%s, %s, %s)",
                            (vacancy[0]["id работодателя"],
                             vacancy[0]["id вакансии"],
                             vacancy[0]["название работодателя"])
                        )
        finally:
        # закрытие соединения
            conn.close()

    def big_red_button(self, table_name):
        """удаляет все данные из указанной таблицы"""
        # Подключение к db
        conn = psycopg2.connect(
            host="localhost",
            database="db_hh_ru",
            user="postgres",
            password=password
        )
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(f"DELETE FROM {table_name}")

        finally:
        # закрытие соединения
            conn.close()