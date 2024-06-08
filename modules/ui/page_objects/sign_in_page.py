import time
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

        # Enter incorrect username or email
        login_elem.send_keys(username)

        # Find the password field 
        pass_elem = self.driver.find_element(By.ID, "password")

        # Enter incorrest password
        pass_elem.send_keys(password)

        # Find the sign in button
        btn_elem = self.driver.find_element(By.NAME, "commit")

        # Search button is clicked
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class Epicentr(BasePage):
    URL = "https://epicentrk.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Epicentr.URL)

    def try_search_product(self, name_product):

        # Find the field for Search input
        search_field = self.driver.find_element(By.XPATH, '//*[@id="global-site-header"]/header/div/div[3]/form/input')

        # Enter the product name
        search_field.send_keys(name_product)

        # Find the Search button
        btn_search = self.driver.find_element(
            By.XPATH, '//*[@id="global-site-header"]/header/div/div[3]/form/button[2]'
        )

        # Search button is clicked
        btn_search.click()

    def check_page_header(self, expected_page_header):
        header_page = self.driver.find_element(By.XPATH, '//*[@id="__template"]/main/div[1]/section/div[1]/h1')
        
        return header_page.text == expected_page_header
    
    def check_order_product(self, expected_header):

        # Find Cart button
        btn_cart = self.driver.find_element(By.XPATH, '//*[@id="__template"]/main/div[1]/section/div[1]/div/div/div[4]/div/ul/li[1]/article/div/div[5]/div/div[2]/button')

        time.sleep(3)

        # Cart button is clicked
        btn_cart.click()

        time.sleep(3)

        # Find the Cart order button
        btn_order = self.driver.find_element(By.XPATH, '//*[@id="__template"]/div[2]/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/button')

        time.sleep(3)

        # Cart order button is clicked
        btn_order.click()

        time.sleep(3)

        # Check page header
        header_page = self.driver.find_element(By.XPATH, '//*[@id="checkout"]/div[2]/div/div/h1')
        
        return header_page.text == expected_header
    
