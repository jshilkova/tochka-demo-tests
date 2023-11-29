from selene import browser, have, be
from selenium.webdriver import Keys

class VacancyPage:
    def assert_vacancy_name(self, value):
        browser.element('h1.mb-6').should(have.exact_text(value))

