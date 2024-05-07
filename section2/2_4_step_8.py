import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:


    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    _ = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку "Book"
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    el = browser.find_element(By.ID, "input_value")
    x = el.text
    print(f"x = {x}")

    # Посчитать математическую функцию от x
    y = calc(x)
    print(f" y = { y}")

    # Ввести ответ в текстовое поле.
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Отправить ответ
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    input("Enter for end")
    # закрываем браузер после всех манипуляций
    browser.quit()