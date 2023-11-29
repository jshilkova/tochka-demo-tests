import allure

from tochka_demo_tests.pages.vacancies_page import VacanciesPage
from tochka_demo_tests.pages.vacancies_page import Specialization
from tochka_demo_tests.pages.vacancies_page import Type
from tochka_demo_tests.pages.vacancy_page import VacancyPage

vacancies = VacanciesPage()
vacancy = VacancyPage()

@allure.tag("web")
@allure.feature("Vacancies")
@allure.title("Open vacancy page from results")
def test_click_on_vacancy_card_should_open_vacancy_page():
    vacancy_name = 'Тестировщик'

    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Click vacancy card"):
        vacancies.open_vacancy(vacancy_name)

    with allure.step("The selected vacancy page opens"):
        vacancy.assert_vacancy_name(vacancy_name)
