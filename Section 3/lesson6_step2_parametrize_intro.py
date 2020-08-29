import pytest

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# parametrize - позволяет запустить тест с разными входными данными (здесь: разный язык страницы)
# Нужно также передать параметр ('language') как аргумент (language, без ковычек)  в тест
# Можно передать, н., tuples:
# #@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42, marks=pytest.mark.xfail)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
# Тест из примера сверху будет запущен 3 раза
# 2 пройдут, 3ий - нет, либо assertion error, либо, как данном случае, отмечен xfail


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

# Можно передать parametrize классу, тогда все тесты этого класса будут запускаться с этими параметрами


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# class TestLogin:
#     # Тест запуститься 2 раза
#     def test_guest_should_see_login_link(self, browser, language):
#         link = f"http://selenium1py.pythonanywhere.com/{language}/"
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     #  Тоже запуститься 2 раза
#     def test_guest_should_see_navbar_element(self, browser, language):
#         pass

# Еще пример:
# #import pytest
#
# from selenium import webdriver
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# languages = [
#     ("ru", "русский"),
#     ("de", "немецкий"),
#     ("ua", "украинский"),
#     ("en-gb", "английский")
# ]
#
#
# @pytest.mark.parametrize("code, lang", languages)
# def test_guest_should_see_login_link(browser, code, lang):
#     link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
#     print("Проверяемый язык %s" % code)

