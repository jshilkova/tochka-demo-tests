import allure
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


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Apply specialization filter")
def test_filter_by_specialization():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Select Маркетинг specialization filter"):
        vacancies.select_specialization(Specialization.marketing.value)

    with allure.step("Check that all filtered vacancies have Маркетинг as specialization"):
        vacancies.assert_all_results_have_specialization(Specialization.marketing.value)


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Switch specialization filter")
def test_switch_filter_by_specialization():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Select IT specialization"):
        vacancies.select_specialization(Specialization.it.value)
    with allure.step("Select Маркетинг specialization"):
        vacancies.select_specialization(Specialization.marketing.value)

    with allure.step("Check that all filtered vacancies have Маркетинг as specialization"):
        vacancies.assert_all_results_have_specialization(Specialization.marketing.value)


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Reset specialization filter")
def test_filter_by_specialization_reset(get_all_vacancies):
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Select IT specialization"):
        vacancies.select_specialization(Specialization.it.value)
    with allure.step("Select Any specialization"):
        vacancies.select_specialization(Specialization.any.value)

    with allure.step("Check that vacancies list is in initial state"):
        assert vacancies.get_result_urls() == get_all_vacancies

@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Apply experience filter")
def test_experience_filter():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply filter by experience"):
        vacancies.select_experience(Experience.none.value)

    with allure.step("Check that the number of filtered vacancies is as expected"):
        expected_vacancies_count = 26
        vacancies.assert_results_count(expected_vacancies_count)
        vacancies.assert_results_count_from_header(expected_vacancies_count)


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Reset experience filter")
def test_experience_filter_reset(get_all_vacancies):
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply filter by experience"):
        vacancies.select_experience(Experience.none.value)
    with allure.step("Click on the same filter again to reset"):
        vacancies.select_experience(Experience.none.value)

    with allure.step("Check that vacancies list is in initial state"):
        assert vacancies.get_result_urls() == get_all_vacancies


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Reset type filter")
def test_type_filter_reset(get_all_vacancies):
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply filter by type"):
        vacancies.select_type(Type.hybrid.value)
    with allure.step("Click on the same filter again to reset"):
        vacancies.select_type(Type.hybrid.value)

    with allure.step("Check that vacancies list is in initial state"):
        assert vacancies.get_result_urls() == get_all_vacancies


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Applied filter by remote job hides filter by city")
def test_selecting_remote_should_hide_city_filter():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply Remote job filter"):
        vacancies.select_type(Type.remote.value)

    with allure.step("Check that filter by city is hidden"):
        vacancies.assert_city_is_hidden()


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Apply salary filter")
def test_salary_filter():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply salary filter"):
        salary = 210000
        vacancies.set_salary(salary)

    with allure.step("Check that all vacancies have"):
        vacancies.assert_all_results_have_salary(salary)


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Apply filter combination")
def test_combination_of_3_filters():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply filter by specialization"):
        vacancies.select_specialization(Specialization.it.value)
    with allure.step("Apply filter by experience"):
        vacancies.select_experience(Experience.one_to_tree.value)
    with allure.step("Apply Remote job filter"):
        vacancies.select_type(Type.remote.value)

    with allure.step("7 vacancies found"):
        vacancies.assert_results_count_from_header(7)
        vacancies.assert_results_count(7)
    with allure.step("Тестировщик vacancy found"):
        vacancies.assert_vacancy_presents('Тестировщик')


@allure.tag("web")
@allure.feature("Vacancy filters")
@allure.title("Apply filter combination with no results")
def test_filters_with_no_results():
    with allure.step("Open vacancies page"):
        vacancies.open()

    with allure.step("Apply filter Без опыта"):
        vacancies.select_experience(Experience.none.value)
    with allure.step("Set high salary"):
        vacancies.set_salary(400000)

    with allure.step("Check that 0 vacancies found"):
        vacancies.assert_results_count_from_header(0)
        vacancies.assert_results_count(0)