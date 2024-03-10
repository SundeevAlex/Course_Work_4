from abc import ABC, abstractmethod
import requests


class MainVacancyAPI(ABC):
    """
    Общий класс для работы с API сервиса с вакансиями
    """
    @abstractmethod
    def get_vacancies(self, url: str):
        pass


class HhVacancy(MainVacancyAPI):
    """
    Класс для работы с API сервиса с вакансиями hh.ru
    """
    def get_vacancies(self, url: str) -> dict:
        """
        Получение вакансий с сайта
        """
        response = requests.get(url, params={'text': 'Python'})
        if response.status_code != 200:
            raise ValueError(f'Ошибка доступа к сайту {url}')
        else:
            response_data = response.json()
        return response_data

