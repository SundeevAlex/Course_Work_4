from src.functions import create_vacancies, filter_vacancies, print_results
from src.functions import get_vacancies_by_salary, sort_vacancies, create_vacancies_from_file
from src.classes import HhVacancy, JSONSaver, Vacancy, JSONLoader


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (<Enter> - без фильтрации): ").lower().split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000), (<Enter> - весь диапазон): ")

    hh_api = HhVacancy()
    hh_vacancies = hh_api.get_vacancies(search_query, top_n)
    vacancies = create_vacancies(hh_vacancies)
    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    JSONSaver(vacancies_list)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    print_results(sorted_vacancies)


if __name__ == "__main__":
    user_interaction()
