import enum

from selene import browser, have, be
from selenium.webdriver import Keys


class Filter(enum.Enum):
    specialization = 'Выбери направление работы'
    experience = 'Опыт работы'
    type = 'Как хочешь работать'
    city = 'Выбери, откуда хочешь работать'
    salary = 'Зарплата'


class Specialization(enum.Enum):
    any = 'Любое'
    it = 'IT'
    business = 'Сопровождение бизнеса'
    marketing = 'Маркетинг'
    sales = 'Продажи'
    support = 'Поддержка'

class Experience(enum.Enum):
    none = 'Без опыта'
    one_to_tree = 'От 1 года до 3 лет'
    three_and_more = 'От 3 лет'

class Type(enum.Enum):
    office = 'В офисе'
    remote = 'Удалённо'
    hybrid = 'Гибридно'


class VacanciesPage:
    def open(self):
        browser.open('/hr/vacancies/')

    def select_specialization(self, value):
        browser.all('.tab_tabButton___PexF').element_by(have.text(value)).click()

    def select_experience(self, value):
        (browser.all('.mb-3').element_by(have.text(Filter.experience.value)).all('.tab_tabButton___PexF')
         .element_by(have.text(value)).click())

    def select_type(self, value):
        (browser.all('.mb-3').element_by(have.text(Filter.type.value)).all('.tab_tabButton___PexF')
         .element_by(have.text(value)).click())

    def set_salary(self, value):
        browser.element('#salary_textInput').type(Keys.CONTROL + 'a' + Keys.NULL).type(value)

    def assert_all_results_have_specialization(self, value):
        for element in browser.all('[class*="jobs_jobsListItem_"]').should(have.no.size(0)):
            element.element('[class*="jobs_item"]:nth-child(2)').should(have.exact_text(value))

    def assert_all_results_have_salary(self, value):
        for element in browser.all('[class*="jobs_jobsListItem_"]').should(have.no.size(0)):
            salary = element.element('[class*="jobs_item"]:nth-child(3)').locate().get_attribute("innerText").split(" ")[1]
            assert int(''.join(salary.split(" "))) >= value

    def assert_results_count(self, value: int):
        browser.all('[class*="jobs_jobsListItem_"]').should(have.size(value))

    def assert_results_count_from_header(self, value: int):
        browser.element('[class^="jobs_jobsSearchMeta_"] p').should(have.text(str(value)))

    def get_result_urls(self):
        return [x.locate().get_attribute('href') for x in browser.all('[class*="jobs_jobsListItem_"] a')]

    def assert_city_is_hidden(self):
        browser.all('.mb-3').element_by(have.text(Filter.city.value)).should(be.not_.present)

    def assert_vacancy_presents(self, value):
        browser.all('[class^="jobs_jobsListItemName"]').element_by(have.text(value)).should(be.present)

    def open_vacancy(self, value):
        browser.all('[class^="jobs_jobsListItemName"]').element_by(have.text(value)).click()
