import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):
    welcome_text = ""
    msg = f"Текст '{welcome_text}' не совпадает с ожидаемым 'Congratulations! You have successfully registered!'"

    def get_text(self, link)-> str:

        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//label[contains(text(),'First name*')]/following-sibling::input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//label[contains(text(),'Last name*')]/following-sibling::input")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Email*')]/following-sibling::input")
        input3.send_keys("ivanov@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        browser.quit()

        return welcome_text

    def test_selectors1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.get_text(link)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, self.msg)

    def test_selectors2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.get_text(link)

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, self.msg)


if __name__ == "__main__":
    unittest.main()