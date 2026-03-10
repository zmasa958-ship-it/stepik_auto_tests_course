from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # Поле First name (обязательное, отмечено *)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name.send_keys("Ivan")
    
    # Поле Last name (обязательное, отмечено *)
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name.send_keys("Petrov")
    
    # Поле Email (обязательное, отмечено *)
    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email.send_keys("ivan.petrov@example.com")
    
    print("Обязательные поля заполнены")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    print("Форма отправлена")

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print(f"Текст на странице: {welcome_text}")

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    expected_text = "Congratulations! You have successfully registered!"
    assert expected_text == welcome_text, f"Ожидался текст '{expected_text}', но получен '{welcome_text}'"
    
    print("Тест успешно пройден!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()