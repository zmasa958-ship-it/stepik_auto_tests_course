import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Вычисляем зашифрованный текст ссылки
encrypted_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(f"Ищем ссылку с текстом: {encrypted_text}")

link = "http://suninjuly.github.io/find_link_text"

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Небольшая пауза для загрузки страницы
    time.sleep(1)
    
    # Находим ссылку по вычисленному тексту и кликаем по ней
    target_link = browser.find_element(By.LINK_TEXT, encrypted_text)
    target_link.click()
    
    # Небольшая пауза для загрузки формы
    time.sleep(1)
    
    # Заполняем форму регистрации
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    # Ждем результат
    time.sleep(3)
    
    # Получаем alert
    alert = browser.switch_to.alert
    print("Проверочный код:", alert.text)
    alert.accept()
    
finally:
    time.sleep(5)
    browser.quit()