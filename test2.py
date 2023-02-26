from selenium import webdriver 
import math
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    # link.click()
    input1 = browser.find_element(by='tag name',value='input')
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value='last_name')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='class name', value='city')
    print(input3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element(by='id',value='country')
    print(input4)
    input4.send_keys("Russia")
    button = browser.find_element(by='xpath', value="//button[text()='Submit']")
    button.click()

finally:
    
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.CSS_SELECTOR, 'input')
#     for element in elements:
#         element.send_keys("Мой ответ")

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(40)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла
