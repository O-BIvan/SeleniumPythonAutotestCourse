import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    # Данный декоратор отмечает тест как "smoke", т.е. его можно запустить отдельно
    # pytest -s -v -m smoke test_name.py (где, -m - mark)
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print(" -> smoke")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print(" -> regression")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Если mark не зарегестрирована, то pytest выдает предупреждения об этом
# Для регистрации  необходимо в корне проекта создать файл pytest.ini
# И добавить туда необходимые mark:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
# Так же можно маркировать целый тестовый класс
# В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс
