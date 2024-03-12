import json
from abc import ABC, abstractmethod
import requests


class MainVacancyAPI(ABC):
    """
    Общий класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self):
        pass


class HhVacancy(MainVacancyAPI):
    """
    Класс для работы с API сервиса с вакансиями hh.ru
    """
    url = 'https://api.hh.ru/vacancies'
    vacancy_name = 'Python'

    def get_vacancies(self) -> dict:
        """
        Получение вакансий с сайта
        """
        response = requests.get(HhVacancy.url, params={'text': HhVacancy.vacancy_name})
        if response.status_code != 200:
            raise ValueError(f'Ошибка доступа к сайту {HhVacancy.url}')
        else:
            response_data = json.loads(response.text)["items"]
        return response_data


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, requirement: str, alternate_url: str, salary_from: float, salary_to: float,
                 salary_currency: float):
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


class AbstractVacancy(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """
    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def get_vacancies_criteria(self):
        pass

    @abstractmethod
    def del_vacancies(self):
        pass


class SaveVacancies:
    """
    Класс для сохранения информации о вакансиях в JSON-файл
    """
    @staticmethod
    def save_to_json(file_name: str, data: dict) -> None:
        """
        Сохранение вакансий в файл JSON
        """
        with open(file_name, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
