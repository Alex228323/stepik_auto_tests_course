from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(by='id',value='num1').text
    num2 = browser.find_element(by='id',value='num2').text
    otvet = str(int(num1)+int(num2))
    input1 = Select(browser.find_element(by=By.TAG_NAME, value='select'))
    input1.select_by_value(otvet)
    button = browser.find_element(by='xpath',value='//button[text()="Submit"]')
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
