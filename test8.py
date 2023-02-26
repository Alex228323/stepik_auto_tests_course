from selenium import webdriver
import math
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(by='name',value='firstname')
    input1.send_keys("Test")
    input1 = browser.find_element(by='name',value='lastname')
    input1.send_keys("Test")
    input1 = browser.find_element(by='name',value='email')
    input1.send_keys("Test")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'Testf.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element(by='id',value='file')
    element.send_keys(file_path)
    button = browser.find_element(by='xpath',value='//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
