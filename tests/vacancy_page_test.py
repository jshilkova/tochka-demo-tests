
from tochka_demo_tests.pages.vacancies_page import VacanciesPage
from tochka_demo_tests.pages.vacancies_page import Specialization
from tochka_demo_tests.pages.vacancies_page import Type
from tochka_demo_tests.pages.vacancy_page import VacancyPage

vacancies = VacanciesPage()
vacancy = VacancyPage()


def test_click_on_vacancy_card_should_open_vacancy_page():
    vacancy_name = 'Тестировщик'
    vacancies.open()

    vacancies.select_specialization(Specialization.it.value)
    vacancies.select_type(Type.remote.value)

    vacancies.open_vacancy(vacancy_name)
    vacancy.assert_vacancy_name(vacancy_name)
