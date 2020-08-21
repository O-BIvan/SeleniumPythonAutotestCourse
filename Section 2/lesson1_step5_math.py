from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция для подсчета
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Поиск элемента со значением для "х"
    # Расчет значения "calc_answer"
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    calc_answer = calc(x)

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
