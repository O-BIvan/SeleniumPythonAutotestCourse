import os
import time

from selenium import webdriver
import pyperclip


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля формы (можно заполнить через "for" loop)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Abc")
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("Xyz")
    input1 = browser.find_element_by_name("email")
    input1.send_keys("123@qwerty.co")

    # Поиск директории, в которой находится текущий файл
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # Указываем путь к файлу, который нужно загрузить (можно пустой)
    file_path = os.path.join(current_dir, 'step8.txt')

    # Ищем элемент (input),котрый нужно инициализировать для загрузки файла
    button_upload = browser.find_element_by_id("file")

    # Отправляем путь к файлу как переменую, как аргумент, для загрузки
    button_upload.send_keys(file_path)

    # Находим и инициализируем кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Копируем число-ответ из окна alert в буфер
    # Должны быть установлены: xclip/xcel, pyperclip в виртуальной среде
    # Спасибо Vitaliy Ya ("https://stepik.org/users/104430773")
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

except Exception as error:
    print(error)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# import os
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/file_input.html')
#
# file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')
#
# if not os.path.exists(file_path):
#     with open(file_path, 'w') as f:
#         pass
#
# inputs = ['Firstname', 'Secondname', 'mail@somemailbox.co', file_path]
#
# for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
#     element.send_keys(value)
#
# browser.find_element_by_css_selector('button.btn').click()

# не забываем оставить пустую строку в конце файла
