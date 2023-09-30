import json
import os

from classes.abstract_class import JSONSaver


class WorkWithJson(JSONSaver):
    """класс для работы с json файлом"""

    file_path = '/vacancy.json'

    def add_vacancy(self, id_vacancy):
        """добавление по id в json файл"""
        if os.path.isfile(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                existing_data.extend(id_vacancy)
            with open(self.file_path, 'r+',
                      encoding='utf-8') as file_add:
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

