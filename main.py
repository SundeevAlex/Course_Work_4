from src.functions import load_from_json, create_vacancies
from src.classes import HhVacancy, JSONSaver, Vacancy

hh_api = HhVacancy()
hh_vacancies = hh_api.get_vacancies()
# print(hh_vacancies)
data = create_vacancies(hh_vacancies)
# print(data)

vacancies_list = Vacancy.cast_to_object_list(data)
print(vacancies_list)
JSONSaver.save_to_json('data/vacancy.json', vacancies_list)

# data = load_from_json()
