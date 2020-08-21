import math
import time

import pyperclip
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"


# Функция для подсчета
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Задаем переменную для webdriver, для краткости
    # Переходим по ссылке
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент-кнопку button
    # Нажимаем на нее
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    # Переключаемся на открывшийся confirm
    # Переходим по ссылке
    confirm = browser.switch_to.alert
    confirm.accept()

    # Находим элемент Х для calc(x) и значение .text для него
    # Переводим найденное str значение в int, и считаем calc(x)
    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    calc_answer = calc(int(x_value))

    # Находим поле для написания ответа
    # Переводим ответ calc_answer в str, отпраляем в поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc_answer)

    # Находим кнопку "Submit"
    # Нажимаем ее
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

    # Копируем число-ответ из окна alert в буфер
    # Закоментировать, если ненужно
    # Должны быть установлены: xclip/xcel, pyperclip в виртуальной среде
    # Спасибо Vitaliy Ya ("https://stepik.org/users/104430773")
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

except Exception as error:
    print(error)

finally:

    # Устанавливаем таймер закрытия браузера
    time.sleep(10)
    # Закрываем браузер и останавливаем webdriver
    browser.quit()

# Пустая строка (newline character) для избежания конфликта в некоторых программах
