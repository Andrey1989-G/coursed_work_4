# from classes.get_from_hhru import HeadHunterAPI
# from classes.input_error import Input_error
#
#
# class Vacancy(Input_error):
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
#     @staticmethod
#     def sorted_vacancy(s=HeadHunterAPI):
#         """Метод сортировки информации из api. По умолчанию HeadHunterAPI"""
#         data = s.get_vacancies(s.keyword)
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

