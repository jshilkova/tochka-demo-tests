import pytest

from tochka_demo_tests.pages.vacancies_page import VacanciesPage
from tochka_demo_tests.pages.vacancies_page import Specialization
from tochka_demo_tests.pages.vacancies_page import Experience
from tochka_demo_tests.pages.vacancies_page import Type
from tochka_demo_tests.pages.vacancy_page import VacancyPage

vacancies = VacanciesPage()
vacancy = VacancyPage()


@pytest.fixture(scope="module", autouse=False)
def get_all_vacancies():
    vacancies.open()
    initial_res = vacancies.get_result_urls()
    return initial_res


def test_filter_by_specialization():
    vacancies.open()

    vacancies.select_specialization(Specialization.it.value)

    vacancies.assert_all_results_have_specialization(Specialization.it.value)


def test_switch_filter_by_specialization():
    vacancies.open()

    vacancies.select_specialization(Specialization.it.value)
    vacancies.select_specialization(Specialization.marketing.value)

    vacancies.assert_all_results_have_specialization(Specialization.marketing.value)


def test_filter_by_specialization_reset(get_all_vacancies):
    vacancies.open()

    vacancies.select_specialization(Specialization.it.value)
    vacancies.select_specialization(Specialization.any.value)

    assert vacancies.get_result_urls() == get_all_vacancies


def test_experience_filter():
    vacancies.open()

    vacancies.select_experience(Experience.none.value)

    expected_vacancies_count = 26
    vacancies.assert_results_count(expected_vacancies_count)
    vacancies.assert_results_count_from_header(expected_vacancies_count)


def test_experience_filter_reset(get_all_vacancies):
    vacancies.open()

    vacancies.select_experience(Experience.none.value)
    vacancies.select_experience(Experience.none.value)

    assert vacancies.get_result_urls() == get_all_vacancies

def test_experience_type_reset(get_all_vacancies):
    vacancies.open()

    vacancies.select_type(Type.hybrid.value)
    vacancies.select_type(Type.hybrid.value)

    assert vacancies.get_result_urls() == get_all_vacancies


def test_selecting_remote_should_hide_city_filter():
    vacancies.open()

    vacancies.select_type(Type.remote.value)

    vacancies.assert_city_is_hidden()


def test_salary_filter():
    vacancies.open()

    salary = 210000
    vacancies.set_salary(salary)

    vacancies.assert_all_results_have_salary(salary)


def test_filters_with_no_results():
    vacancies.open()

    vacancies.select_experience(Experience.none.value)
    vacancies.set_salary(400000)

    vacancies.assert_results_count_from_header(0)
    vacancies.assert_results_count(0)


def test_combination_of_3_filters():
    vacancies.open()

    vacancies.select_specialization(Specialization.it.value)
    vacancies.select_experience(Experience.one_to_tree.value)
    vacancies.select_type(Type.remote.value)

    vacancies.assert_results_count_from_header(7)
    vacancies.assert_results_count(7)
    vacancies.assert_vacancy_presents('Тестировщик')
