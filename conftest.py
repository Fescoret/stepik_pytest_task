import pytest
from selenium import webdriver

languages = ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr",
             "it", "ko", "nl", "pl", "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-cn"]

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru/es/fr/en-gb/etc.")


@pytest.fixture(scope="function")
def link(request):
    language = request.config.getoption("language")
    if language in languages:
        link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("--language should be in short format")
    yield link

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
