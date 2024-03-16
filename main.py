from src.functions import create_vacancies, filter_vacancies, print_results
from src.functions import get_vacancies_by_salary, sort_vacancies
from src.classes import HhVacancy, JSONSaver, Vacancy


def user_interaction():
    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").lower().split()
    # salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
    search_query = 'Python'
    top_n = 2
    filter_words = ''.lower().split()
    salary_range = ''

    hh_api = HhVacancy()
    hh_vacancies = hh_api.get_vacancies(search_query, top_n)
    vacancies = create_vacancies(hh_vacancies)
    vacancies_list = Vacancy.cast_to_object_list(vacancies)
    # v1 = Vacancy('Стажер', 'Не важен опыт.', 'https://mail.ru', 50000, 80000, 'RUR')
    json_saver = JSONSaver(vacancies_list)
    # json_saver.add_vacancy(v1)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    print_results(sorted_vacancies)
    # data = load_from_json()


if __name__ == "__main__":
    user_interaction()
