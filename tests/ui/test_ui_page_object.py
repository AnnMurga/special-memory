import pytest
import time
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import NovaPoshta



@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення об'єкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер
    sign_in_page.close()


# Additional tests for Nova Poshta


@pytest.mark.ui_np
def test_check_incorrect_cargo_number_page_object():
    # створення об'єкту сторінки
    np_page = NovaPoshta()

    # відкриваємо сторінку https://novaposhta.ua/
    np_page.go_to()

    time.sleep(3)

    np_page.close_banner()

    # виконуємо спробу знайти неіснуючу накладну
    np_page.try_search_package(12345546)

    time.sleep(3)

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert np_page.check_tracking_error_message(
        "Ми не знайшли посилку за таким номером. Можливо, вона ще не передана для відправлення, або номер некоректний. \
            Перевірте, чи відповідає вказаний номер можливому формату: 59500000031324 або AENM0002497278NPI."
    )

    time.sleep(3)

    # закриваємо браузер
    np_page.close()
