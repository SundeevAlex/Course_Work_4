import json
from src.classes import Vacancy


VACANCY_FILE = 'data/vacancy.json'


def load_from_json() -> dict:
    """
    Загрузка вакансий из файла JSON
    """
    with open(VACANCY_FILE, encoding='utf-8') as file:
        content = file.read()
        file_data = json.loads(content)
    return file_data


def create_vacancies(data):
    """
    Создание объектов красса вакансии
    """
    vacancy = []
    for el in data:
        try:
            requirement = el["snippet"]["requirement"]
            if '<highlighttext>' in requirement:
                requirement = requirement.replace('<highlighttext>', '')
                requirement = requirement.replace('</highlighttext>', '')
            salary_from = el['salary']['from']
            salary_to = el['salary']['to']
            currency = el['salary']['currency']
        except TypeError:
            salary_from = None
            salary_to = None
            currency = None
        vacancy.append(Vacancy(el['name'], requirement, el['alternate_url'], salary_from, salary_to, currency))

    for el in vacancy:
        print(el)
