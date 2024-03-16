from src.functions import filter_vacancies, get_vacancies_by_salary


def test_filter_vacancies():
    assert filter_vacancies([{'name': 'Frontend-разработчик',
                              'requirement': 'Отличное знание CSS3',
                              'alternate_url': 'https://hh.ru/vacancy/94675402',
                              'salary_from': 170000,
                              'salary_to': 210000,
                              'salary_currency': 'RUR'}], ['отличное']) == [{'name': 'Frontend-разработчик',
                                                                             'requirement': 'Отличное знание CSS3',
                                                                             'alternate_url': 'https://hh.ru/vacancy/94675402',
                                                                             'salary_from': 170000,
                                                                             'salary_to': 210000,
                                                                             'salary_currency': 'RUR'}]


def test_get_vacancies_by_salary_agree():
    assert get_vacancies_by_salary([{'name': 'Frontend-разработчик',
                                     'requirement': 'Отличное знание CSS3',
                                     'alternate_url': 'https://hh.ru/vacancy/94675402',
                                     'salary_from': 170000,
                                     'salary_to': 210000,
                                     'salary_currency': 'RUR'}], '0 - 170000') == [{'name': 'Frontend-разработчик',
                                                                                    'requirement': 'Отличное знание CSS3',
                                                                                    'alternate_url': 'https://hh.ru/vacancy/94675402',
                                                                                    'salary_from': 170000,
                                                                                    'salary_to': 210000,
                                                                                    'salary_currency': 'RUR'}]


def test_get_vacancies_by_salary_disagree():
    assert get_vacancies_by_salary([{'name': 'Frontend-разработчик',
                                     'requirement': 'Отличное знание CSS3',
                                     'alternate_url': 'https://hh.ru/vacancy/94675402',
                                     'salary_from': 170000,
                                     'salary_to': 210000,
                                     'salary_currency': 'RUR'}], '0 - 100') == []
