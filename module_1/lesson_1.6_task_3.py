from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Заполняем форму регистрации
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Находим кнопку Submit по XPath и нажимаем её
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
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