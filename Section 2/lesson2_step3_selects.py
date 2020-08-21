from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск слогаемых
    value1_search = browser.find_element_by_id("num1")
    value1 = value1_search.text

    value2_search = browser.find_element_by_id("num2")
    value2 = value2_search.text

    # Вычисление суммы + преобразование в тип строка
    value_sum = str(int(value1) + int(value2))

    # Поиск списка и текста "value_sum" в нем
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(value_sum)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

except Exception as error:
    print(f'Произошла ошибка: {error}')

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

