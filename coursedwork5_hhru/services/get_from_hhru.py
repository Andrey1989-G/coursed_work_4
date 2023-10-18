import requests
from services.abstract_class import GetInfo


class HeadHunterAPI(GetInfo):
    """Класс для получения вакансий с hh"""

    def __init__(self):
        self.keyword = None
        self.per_page = None
        self.info = None

    def get_vacancies(self, keyword: str):
        """поиск вакансии по ключевому слову, которое вводит пользователь"""
        self.keyword = keyword
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.keyword
        }
        response = requests.get(url, params=params)
        vacancies = response.json()
        return vacancies

#
# s = HeadHunterAPI()
# # print(len(s.get_vacancies('ситно')))
# res = s.get_vacancies('ситно')
# for i in res['items']:
#     print(i)