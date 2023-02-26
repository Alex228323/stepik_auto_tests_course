from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(by='xpath',value='//img[@id="treasure"]').get_attribute("valuex")
    print(x_element)
    x = x_element
    y = calc(x)
    # Ваш код, который заполняет обязательные поля//input[@id="robotsRule"]
    input1 = browser.find_element(by='xpath',value='//input[@id="answer"]')
    print(input1)
    input1.send_keys(y)
    radio = browser.find_element(by='xpath',value='//input[@id="robotsRule"]')
    radio.click()
    checkbox = browser.find_element(by='xpath',value='//input[@id="robotCheckbox"]')
    checkbox.click()
    # Отправляем заполненную формуSubmit
    button = browser.find_element(by='xpath',value='//button[text()="Submit"]')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
