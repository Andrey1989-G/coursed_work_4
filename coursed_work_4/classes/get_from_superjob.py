import os
from classes.abstract_class import GetInfo
import requests
from classes.abstract_class import GetInfo
from classes.input_error import Input_error


class SuperJobAPI(GetInfo):
    """Класс для получения вакансий с superjob"""

    def __init__(self):
        self.keyword = None
        self.per_page = None
        self.info = None

    def get_vacancies(self, keyword):
        """поиск вакансии по ключевому слову, которое вводит пользователь"""
        key = os.environ.get("SUPERJOB_API_KEY")
        self.keyword = keyword
        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {
            'X-Api-App-Id': key
        }
        params = {
            'keyword': keyword
        }
        response = requests.get(url, headers=headers, params=params)
        vacancies = response.json()
        return vacancies

# s = SuperJobAPI()
# print(s.get_vacancies('инженер'))

# будет скучно, объединить класс VacancySuperJob и Vacancy
class VacancySuperJob(SuperJobAPI, Input_error):
    """методы работы с вакансиями"""

    def __init__(self, vacancy_id=None, vacancy_name=None,
                 vacancy_url=None, vacancy_salary=None,
                 vacancy_city=None, vacancy_requirement=None,
                 vacancy_responsibility=None):
        try:
            self.vacancy_id = vacancy_id
            self.vacancy_name = vacancy_name
            self.vacancy_url = vacancy_url
            self.vacancy_salary = vacancy_salary
            self.vacancy_city = vacancy_city
            self.vacancy_requirement = vacancy_requirement
            self.vacancy_responsibility = vacancy_responsibility
        except Input_error as s:
            print(s.message)

    def sorted_vacancy(self):
        """
        Метод сортировки информации из api hh в универсальный
        """
        data = self.get_vacancies(self.keyword)
        sorted_vacancy = []
        for item in data['objects']:
            salary = f"{item['payment_from']}-{item['payment_to']}, валюта {item['currency']}"
            info = str(item['candidat'])
            start_index_requir = info.find('Обязанности')
            start_index_resp = info.find('Требования')
            end_index_requir = info.find('Требования') if info.find('Требовани') != -1 else len(info)
            end_index_resp = info.find('Условия:') if info.find('Условия:') != -1 else len(info)
            requirement = info[start_index_requir:end_index_requir] if start_index_requir != -1 \
                                                                       and end_index_requir != -1 else info
            responsibility = info[start_index_resp:end_index_resp] if start_index_resp != -1 \
                                                                      and end_index_resp != -1 else info
            vacancy = {
                "id вакансии": int(item['id']),
                "Название вакансии": item['profession'],
                "Заработная плата": salary,
                "Город": item['town']['title'],
                "Требование": responsibility,
                "Обязанности": requirement,
                "https cсылка": item['link']
            }

            sorted_vacancy.append(vacancy)
        return sorted_vacancy

    def sort_by(self, info, per_page):
        """сортировка вакансий"""
        self.per_page = per_page
        self.info = info
        sorted_vacancy = self.sorted_vacancy()
        if sorted_vacancy:
            sorted_by_city = []
            for i in sorted_vacancy:
                if self.info is not None and self.info in i['Город']:
                    sorted_by_city.append(i)
                else:
                    sorted_vacancy.sort(key=lambda i: i.get(self.info, ''), reverse=True)
            else:
                return sorted_vacancy[:self.per_page]
        else:
            raise Input_error

    def to_dict(self):
        """переводим в словарь"""
        return {
            "id вакансии:": self.vacancy_id,
            "Название:": self.vacancy_name,
            "cсылка:": self.vacancy_url,
            "Заработная плата:": self.vacancy_salary,
            "Город:": self.vacancy_city,
            "Требование:": self.vacancy_requirement,
            "Обязанности:": self.vacancy_responsibility
        }

