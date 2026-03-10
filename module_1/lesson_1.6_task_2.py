from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим все элементы input на странице
    elements = browser.find_elements(By.TAG_NAME, "input")
    
    # Заполняем каждое поле произвольным текстом
    for element in elements:
        element.send_keys("Мой ответ")
    
    # Находим и нажимаем кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Ждем появления результата
    time.sleep(5)
    
    # Получаем alert с проверочным кодом
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()