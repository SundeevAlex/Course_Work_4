import json

VACANCY_FILE = 'data/vacancy.json'

 
def save_to_json(data: dict) -> None:
    """
    Сохранение вакансий в файл JSON
    """
    with open(VACANCY_FILE, "w", encoding='utf-8') as f:
        json.dump(data, f)


def load_from_json() -> dict:
    """
    Загрузка вакансий из файла JSON
    """
    with open(VACANCY_FILE, encoding='utf-8') as file:
        content = file.read()
        file_data = json.loads(content)
    for i in range(20):
        try:
            print('Должность:', file_data['items'][i]["name"])
            s = file_data['items'][i]["snippet"]["requirement"]
            s = s.replace('<highlighttext>', '')
            s = s.replace('</highlighttext>', '')
            print('Требование:', s)
            print(file_data['items'][i]["alternate_url"])
            print(file_data['items'][i]["salary"]["from"])
            print(file_data['items'][i]["salary"]["to"])
            print(file_data['items'][i]["salary"]["currency"])
        except TypeError:
            print('None')
        print(i)
    return file_data
