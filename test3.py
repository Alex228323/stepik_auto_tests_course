from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(by='xpath',value='//input[@class="form-control first"]')
    print(input1)
    input1.send_keys("Ivan")
    input3 = browser.find_element(by='xpath', value='//input[@class="form-control second"]')
    print(input3)
    input3.send_keys("Smolensk")
    input2 = browser.find_element(by='xpath', value='//input[@class="form-control third"]')
    print(input2)
    input2.send_keys("Email")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()
