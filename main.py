from src.functions import create_vacancies
from src.classes import HhVacancy, JSONSaver, Vacancy

hh_api = HhVacancy()
hh_vacancies = hh_api.get_vacancies('Python', 3)
# print(hh_vacancies)
vacancies = create_vacancies(hh_vacancies)
# print(vacancies)

vacancies_list = Vacancy.cast_to_object_list(vacancies)
# print(vacancies_list)

# v1 = Vacancy('Стажер', 'Не важен опыт.', 'https://mail.ru', 50000, 80000, 'RUR')
json_saver = JSONSaver(vacancies_list)
# json_saver.add_vacancy(v1)

# data = load_from_json()
