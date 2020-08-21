import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pyperclip
import selenium_math_calc

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Selenium ждет появление текста (в данном случае $100) в течении 15 сек, и после нахождения нажимает на кнопку
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
      )
    button = browser.find_element_by_id("book")
    button.click()

    # Поиск элемента и его значения для расчета "calc_answer"
    # Расчет значения "calc_answer"
    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    calc_answer = selenium_math_calc.calc(int(x_value))

    # Поиск и заполнение строки значением "calc_answer"
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(calc_answer))

    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()

    # Копируем число-ответ из окна alert в буфер
    # Закоментировать, если не нужно
    # Должны быть установлены: xclip/xcel, pyperclip в виртуальной среде
    # Спасибо Vitaliy Ya ("https://stepik.org/users/104430773")
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    time.sleep(5)
    browser.quit()
