import json
from abc import ABC, abstractmethod
import requests

VACANCY_FILE = 'data/vacancy.json'


class MainVacancyAPI(ABC):
    """
    Общий класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, vacancy_name, top_n):
        pass


class HhVacancy(MainVacancyAPI):
    """
    Класс для работы с API сервиса с вакансиями hh.ru
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, vacancy_name, top_n) -> dict:
        """
        Получение вакансий с сайта
        """
        response = requests.get(self.url, params={'text': vacancy_name, 'per_page': top_n})
        if response.status_code != 200:
            raise ValueError(f'Ошибка доступа к сайту {self.url}')
        else:
            response_data = json.loads(response.text)["items"]
        return response_data


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, requirement: str, alternate_url: str, salary_from: float, salary_to: float,
                 salary_currency: str):
        self.name = name
        self.requirement = requirement
        self.alternate_url = alternate_url
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.salary_currency = salary_currency

        # Валидация данных
        if not self.__salary_from:
            self.__salary_from = 0

        if not self.__salary_to:
            self.__salary_to = 0

        if not self.salary_currency:
            self.salary_currency = "Нет информации о валюте з/п"

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from

    def __repr__(self):
        return (
            f'Vacancy: {self.name}\n {self.requirement}\n {self.alternate_url}\n {self.__salary_from}\n {self.__salary_to}\n '
            f'{self.salary_currency}\n')

    @staticmethod
    def cast_to_object_list(data: list) -> list:
        """
        # Преобразование набора данных из JSON в список объектов
        """
        vacancies_list = []
        for i in range(len(data)):
            el = {
                "name": data[i].name,
                "requirement": data[i].requirement,
                "alternate_url": data[i].alternate_url,
                "salary_from": data[i].__salary_from,
                "salary_to": data[i].__salary_to,
                "salary_currency": data[i].salary_currency
            }
            vacancies_list.append(el)
        return vacancies_list

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to


# class JSONLoader:
#     """
#     Класс для загрузки информации о вакансиях из JSON-файла
#     """
#
#     @staticmethod
#     def load_from_json() -> dict:
#         with open(VACANCY_FILE, encoding='utf-8') as file:
#             content = file.read()
#             file_data = json.loads(content)
#         return file_data


class AbstractVacancy(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def add_vacancy(self, data):
        pass

    @abstractmethod
    def get_vacancies_criteria(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(AbstractVacancy):

    def __init__(self, data):
        self.data = data
        with open(VACANCY_FILE, "w", encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def add_vacancy(self, vacancy) -> dict:
        """
        Добавление вакансии
        """
        el = {
            "name": vacancy.name,
            "requirement": vacancy.requirement,
            "alternate_url": vacancy.alternate_url,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "salary_currency": vacancy.salary_currency
        }
        self.data.append(el)
        return self.data

    def get_vacancies_criteria(self):
        pass

    def delete_vacancy(self):
        pass
