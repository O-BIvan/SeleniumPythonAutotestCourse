import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():  # Вызывается для каждого КЕЙСА в СЦЕНАРИИ
    print("\nstart browser for test..")  # Потому что фикстура для метода def test_.., а не для класса class Test..
    browser = webdriver.Chrome()
    yield browser
    # Этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    # Вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):  # Открывается браузер
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")  # Находим элемент, закрываем браузер

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):  # Открываем браузер
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")  # Находим элемент, закрываем браузер
