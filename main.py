from src.functions import load_from_json, create_vacancies
from src.classes import HhVacancy, SaveVacancies

hh_api = HhVacancy()
hh_vacancies = hh_api.get_vacancies()
SaveVacancies.save_to_json('data/vacancy.json', hh_vacancies)

data = load_from_json()
# print(data)
create_vacancies(data)
