from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Функция для подсчета
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Поиск элемента и его значения для расчета "calc_answer"
    # Расчет значения "calc_answer"
    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    calc_answer = calc(int(x_value))

    # Поиск и заполнение строки значением "calc_answer"
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(calc_answer))

    # Прокручиваем страницу до кнопки "Submit"
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

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

