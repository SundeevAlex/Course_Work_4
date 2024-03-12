from src.functions import save_to_json, load_from_json, create_vacancies
from src.classes import HhVacancy

# hh_api = HhVacancy()
# hh_vacancies = hh_api.get_vacancies()
# print(hh_vacancies)
# save_to_json(hh_vacancies)

data = load_from_json()
# print(data)
create_vacancies(data)
