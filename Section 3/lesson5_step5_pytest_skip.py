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


skip = "yes"
# skip = "no"


class TestSkipThis:
    # mark встроенная в pytest - пропускает тест, вне зависимости от условий
    # Данный тест
    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    # skipif - пропускает тест в зависимости от условий
    # В данном случае отталкиваясь от значения skip
    # Если задать ей значение отличное от "yes", то тест пропущен НЕ будет
    # reason будет выведен, если добавить флаг -rs
    @pytest.mark.skipif(skip == "yes", reason="Skipped because skip = yes")
    def test_skip_if(self):
        print("\n Not skipped")

