from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция для подсчета
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Поиск элемента и его valuex, содержащим значение для расчета "calc_answer"
    # Расчет значения "calc_answer"
    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")
    calc_answer = calc(x_value)
    # valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')

    # Поиск и заполнение строки значением "calc_answer"
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc_answer)

    # Отмечаем "I'm the robot" checkbox
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # Отмечаем "Robots rule" radiobutton
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
