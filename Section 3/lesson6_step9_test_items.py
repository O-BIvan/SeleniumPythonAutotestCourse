import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_btn_present(browser):
    browser.get(link)
    time.sleep(30)
    # Используется find_elementS, для получения списка элементов
    basket_btn = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(basket_btn) == 1, "Element 'Add to basket' not found or CSS_SELECTOR not unique"
