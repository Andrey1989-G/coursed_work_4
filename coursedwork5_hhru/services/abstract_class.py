from abc import ABC, abstractmethod


class GetInfo(ABC):
    """Абстрактный класс и метод для получения информации через API"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class JSONSaver(ABC):
    """абстрактный класс для работы с json"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by(self, salary: str):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass