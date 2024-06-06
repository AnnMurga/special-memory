from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Find the field where input username or email
        login_elem = self.driver.find_element(By.ID, "login_field")

        # вводимо неправильне ім'я користувача або поштову адресу
        # Enter username or email
        login_elem.send_keys(username)

        # знаходимо поле, в яке будемо вводити неправильний пароль
        pass_elem = self.driver.find_element(By.ID, "password")

        # вводимо неправильний пароль
        pass_elem.send_keys(password)

        # знаходимо кнопку sign in
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # емулюємо клік лівою кнопки миші
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class NovaPoshta(BasePage):
    URL = "https://novaposhta.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(NovaPoshta.URL)

    def try_search_package(self, num):
        # знаходимо поле, в яке будемо вводити номер накладної
        cargo_number = self.driver.find_element(By.ID, "cargo_number")

        # вводимо неправильний номер накладної
        cargo_number.send_keys(num)

        # знаходимо кнопку submit
        btn_elem = self.driver.find_element(
            By.XPATH, '//*[@id="top_block"]/div[1]/div/div[2]/form/input[2]'
        )

        # емулюємо клік лівою кнопки миші
        btn_elem.click()

    def check_tracking_error_message(self, expected_text):
        tracking_error_message = self.driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/section/div/div/div[2]/div/text()')
        return tracking_error_message == expected_text
        

    def close_banner(self):
        self.driver.find_element(By.XPATH, '//*[@id="popup_info"]/div[1]/i').click()
