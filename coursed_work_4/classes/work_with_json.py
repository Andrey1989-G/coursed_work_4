import json
import os

from classes.abstract_class import JSONSaver, GetInfo
from classes.input_error import Input_error


class WorkWithJson(JSONSaver):
    """класс для работы с json файлом"""
    file_path = 'data/vacancy.json'

    def get_vacancies(self):
        """получение информации из файла"""
        with open(self.file_path, 'r', encoding='utf-8') as file:
            s = json.load(file)
            return s

    def add_vacancy(self, id_vacancy):
        """добавление по id в json файл"""
        if os.path.isfile(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                existing_data.extend(id_vacancy)
            with open(self.file_path, 'r+', encoding='utf-8') as file_add:
                json.dump(existing_data, file_add, ensure_ascii=False, indent=4)
                return
        else:
            with open(self.file_path, 'w', encoding='utf-8') as file_add:
                json.dump(id_vacancy, file_add, ensure_ascii=False, indent=4)
                return

    def delete_vacancy(self, id_vacancy):
        """удаление по id из json"""
        if os.path.isfile(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for i in data:
                    if i['id вакансии:'] == id_vacancy:
                        data.remove(i)
                with open(self.file_path, 'w', encoding='utf-8') as file_del:
                    json.dump(data, file_del, ensure_ascii=False, indent=4)
                    return

    def get_vacancies_by(self, id_vacancy_i, id_vacancy_j=None):
        """получение информации о вакансии по её id"""
        if os.path.isfile(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                salary = []
                for i in data:
                    if i['id вакансии:'] == id_vacancy_i and id_vacancy_j is None:
                        for key, value in i.items():
                            print(key, value)
                    elif id_vacancy_j is not None:
                        if i["id вакансии:"] == id_vacancy_i or i["id вакансии:"] == id_vacancy_j:
                            salary.append(i["Заработная плата:"])
                return salary

# class Vacancy_local(WorkWithJson,Input_error):
#     """методы работы с вакансиями"""
#
#     def __init__(self, vacancy_id=None, vacancy_name=None, vacancy_url=None,
#                  vacancy_salary=None, vacancy_city=None, vacancy_requirement=None,
#                  vacancy_responsibility=None):
#         try:
#             self.vacancy_id = vacancy_id
#             self.vacancy_name = vacancy_name
#             self.vacancy_url = vacancy_url
#             self.vacancy_salary = vacancy_salary
#             self.vacancy_city = vacancy_city
#             self.vacancy_requirement = vacancy_requirement
#             self.vacancy_responsibility = vacancy_responsibility
#         except Input_error as s:
#             print(s.message)
#
#     def sorted_vacancy(self):
#         """Метод сортировки информации из api"""
#         data = self.get_vacancies(self.keyword)
#         sorted_vacancy = []
#         for item in data['items']:
#             salary = item['salary']
#             salary_range = f"{salary['from']}-{salary['to']}, валюта {salary['currency']}" if salary and salary[
#                 'from'] and salary['to'] else "Не указано"
#             vacancy = {
#                 "id вакансии": int(item['id']),
#                 "Название": item['name'],
#                 "Заработная плата": salary_range,
#                 "Город": item["area"]["name"],
#                 "Требование": item['snippet']['requirement'],
#                 "Обязанности": item['snippet']['responsibility'],
#                 "cсылка": item['url']
#             }
#             sorted_vacancy.append(vacancy)
#         return sorted_vacancy
#
#     def sort_by(self, info, per_page):
#         """сортировка вакансий"""
#         self.per_page = per_page
#         self.info = info
#         sorted_vacancy = self.sorted_vacancy()
#         if sorted_vacancy:
#             sorted_by_city = []
#             for i in sorted_vacancy:
#                 if self.info is not None and self.info in i['Город']:
#                     sorted_by_city.append(i)
#                 else:
#                     sorted_vacancy.sort(key=lambda i: i.get(self.info, ''), reverse=True)
#             else:
#                 return sorted_vacancy[:self.per_page]
#         else:
#             raise Input_error
#
#     def to_dict(self):
#         """переводим в словарь"""
#         return {
#             "id вакансии:": self.vacancy_id,
#             "Название:": self.vacancy_name,
#             "cсылка:": self.vacancy_url,
#             "Заработная плата:": self.vacancy_salary,
#             "Город:": self.vacancy_city,
#             "Требование:": self.vacancy_requirement,
#             "Обязанности:": self.vacancy_responsibility
#         }