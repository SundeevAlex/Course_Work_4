import json
from src.classes import Vacancy


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
    return vacancy


def filter_vacancies(vacancies: list, words: list) -> list:
    """
    Фильтрация вакансий по ключевым словам
    """
    vacancies_filter = [vacancy for vacancy in vacancies if
                        any(key in vacancy['requirement'].lower() for key in words)]
    if not words:
        vacancies_filter = vacancies
        print('\nНе заданы ключевые слова для фильтрации вакансий.')
    return vacancies_filter


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    salary_range = salary_range.split(' - ')
    try:
        min_salary = int(salary_range[0])
        max_salary = int(salary_range[1])
    except ValueError:
        print('\nНе задан диапазон зарплат.\n')
        return vacancies
    except IndexError:
        print('\nНе задан диапазон зарплат.\n')
        return vacancies
    if min_salary < max_salary and max_salary > 0:
        filtered_vacancies = [vacancy for vacancy in vacancies if
                              max_salary >= vacancy['salary_from'] >= min_salary]
    else:
        print('\nНеверно задан диапазон зарплат.\n')
        return vacancies
    return filtered_vacancies


def sort_vacancies(ranged_vacancies) -> list:
    sorted_vacancies = sorted(ranged_vacancies, key=lambda vacancy: vacancy.get('salary_from', 0), reverse=True)
    return sorted_vacancies


def print_results(vacancy) -> None:
    if not vacancy:
        print('\nПо данному запросу вакансий не найдено.')
    else:
        for el in vacancy:
            print(f'Вакансия: {el["name"]}')
            print(f'Требования: {el["requirement"]}')
            print(f'Зароботная плата от {el["salary_from"]} до {el["salary_to"]}, {el["salary_currency"]}.')
            print(f'Ссылка: {el["alternate_url"]}\n')
