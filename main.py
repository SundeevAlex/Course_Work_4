from src.functions import save_to_json, load_from_json
from src.classes import HhVacancy

# save_to_json(data)

hh_api = HhVacancy()

hh_vacancies = hh_api.get_vacancies('https://api.hh.ru/vacancies')
# print(hh_vacancies)
load_from_json()
