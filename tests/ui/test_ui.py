import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # відкриваємо сторінку
    driver.get("https://github.com/login")

    # знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, 'login_field')

    # вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # знаходимо кнопку sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # емулюємо клік лівою кнопки миші
    btn_elem.click()

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'

    #time.sleep(3)

    # закриваємо браузер
    driver.close()