import pytest

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# Scope - к чему применяется фикстура, в данном случае к class TestMainPage
# Если class несколько, то применяется ко всем
# Yield - генератор (создает данные, когда есть запрос, и не харанит их после) см. генераторы и итераторы
# В данном случае: yield - возвращает свое значение (browser), до того момента пока есть список иттерируемых объектов
# В нашем случае эти объекты - список все тестов (def test_...)
# Как только список закончиться - срабатывает код после yield (...browser.quit())


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    # Вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")


class TestMainPage2:  # для проверки применения фикстуры

    def test_guest_should_see_login_link(self, browser):
        print("start test3 - different suite")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test3 - different suite")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test4 - different suite")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test4 - different suite")

