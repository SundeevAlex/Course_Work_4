import requests

VACANCY_FILE = 'vacancy.json'


def get_vacancy(url):
    """
    Получение вакансий с сайта hh.ru
    """
    response = requests.get(url, params={'text': 'Python'})
    print(response.status_code)
    response_data = response.json()
    print(response_data)
