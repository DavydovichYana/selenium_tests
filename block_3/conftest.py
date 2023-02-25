import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# # @pytest.fixture(scope="function")
# # def browser():
# #     print("\nstart browser for test..")
# #     browser = webdriver.Chrome()
# #     yield browser
# #     # этот код выполнится после завершения теста
# #     print("\nquit browser..")
# #     browser.quit()
#
# # @pytest.fixture(scope="function")
# # def browser():
# #     print("\nstart browser for test..")
# #     chrome_options = Options()
# #     chrome_options.add_argument("--headless")  # мы не видим открытие окон
# #     browser = webdriver.Chrome(options=chrome_options)
# #     yield browser
# #     print("\nquit browser..")
# #     browser.quit()