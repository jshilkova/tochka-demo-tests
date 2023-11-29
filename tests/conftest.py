import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.base_url = 'https://tochka.com/'

    yield

    browser.quit()


