from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля с использованием уникальных селекторов
    
    # Поле First name (первое поле в первом блоке)
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    first_name.send_keys("Ivan")
    
    # Поле Last name (второе поле в первом блоке)
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    last_name.send_keys("Petrov")
    
    # Поле Email (третье поле в первом блоке)
    email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    email.send_keys("ivan.petrov@example.com")
    
    print("Обязательные поля заполнены")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст подтверждения
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    print(f"Текст на странице: {welcome_text}")

    # Проверяем, что регистрация прошла успешно
    expected_text = "Congratulations! You have successfully registered!"
    assert expected_text == welcome_text, f"Ожидался текст '{expected_text}', но получен '{welcome_text}'"
    
    print("Тест успешно пройден!")

finally:
    # Ожидание для визуальной оценки
    time.sleep(5)
    # Закрываем браузер
    browser.quit()