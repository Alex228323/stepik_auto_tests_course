from selenium import webdriver
import math
import time

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(by='xpath',value='//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(by='xpath',value='//input[@class="form-control"]')
    input1.send_keys(y)
    checkbox = browser.find_element(by='xpath',value='//input[@id="robotCheckbox"]')
    checkbox.click()
    radio = browser.find_element(by='xpath',value='//input[@id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(by='xpath',value='//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
