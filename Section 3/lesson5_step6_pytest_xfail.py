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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # Данный тест помечен как xfail тк, допустим, данной функции пока нет, но планируется в дальнейшем
    # Тест будет отмечаться как XFAIL, но тест-СЦЕНАРИЙ будет проходить на 100% (при условии выполнения других тестов)
    # Когда на страницу добавят эту кнопку, тест будет проходить как XPASS
    # Тогда .xfail можно будет убрать
    # можно добавить пояснение (reason) к тесту, вызывается флагом -rsx, -rA
    @pytest.mark.xfail(reason="---Not implemented yet---")
    def test_guest_should_see_important_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.important")

    # Данный тест показывает, что будет, если тест с xfail пройдет (XPASS)
    @pytest.mark.xfail(reason="---Not implemented yet---")
    def test_guest_should_see_important_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")
