import unittest

from selenium import webdriver


class TestReg2(unittest.TestCase):
    def test_reg2(self):  # здесь не использовать try/except
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # first block
        input1 = browser.find_element_by_css_selector("div.first_block input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.form-control.third")
        input3.send_keys("abc@abc.com")
        # second block
        input4 = browser.find_element_by_css_selector("div.second_block input.form-control.first")
        input4.send_keys("12345")
        input4 = browser.find_element_by_css_selector("div.second_block input.form-control.second")
        input4.send_keys("street")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_actual = welcome_text_elt.text
        # записываем в переменную ожидаемый текст
        welcome_text_expected = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text_expected, welcome_text_actual, "Expected welcome text != Actual welcome text")


if __name__ == "__main__":
    unittest.main()
