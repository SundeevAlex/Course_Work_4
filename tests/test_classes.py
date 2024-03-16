import pytest
from src.classes import Vacancy


@pytest.fixture
def class_vacancy():
    return Vacancy("Стажер-разработчик Python",
                   "Не важен опыт, важно стремление к постоянному росту и мотивация.",
                   "https://hh.ru/vacancy/94402102",
                   2400,
                   0,
                   "BYR")


def test_vacancy_init(class_vacancy):
    assert class_vacancy.name == "Стажер-разработчик Python"
    assert class_vacancy.requirement == "Не важен опыт, важно стремление к постоянному росту и мотивация."
    assert class_vacancy.alternate_url == "https://hh.ru/vacancy/94402102"
    assert class_vacancy.salary_currency == "BYR"
