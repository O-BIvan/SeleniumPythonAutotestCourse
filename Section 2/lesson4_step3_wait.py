from selenium import webdriver
import time

# Кнопка отрисовывается с задержкой, поэтому тест падает, не найдя ее.
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

time.sleep(10)
browser.quit()