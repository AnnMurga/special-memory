import pytest
import time
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.sign_in_page import Epicentr



@pytest.mark.ui
def test_check_incorrect_username_page_object():

    # Create page object
    sign_in_page = SignInPage()

    # Open page https://github.com/login
    sign_in_page.go_to()

    # Try to log in to GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong_password")

    # Check that the title page is as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close browser
    sign_in_page.close()


# Additional tests for Epicentr


@pytest.mark.ui
def test_check_correct_page_header_page_object():

    # Create page object
    epic_page = Epicentr()

    # Open page https://epicentrk.ua/
    epic_page.go_to()

    time.sleep(3)

    # Try to search product
    search_product = 'Шезлонг'
    epic_page.try_search_product(search_product)

    time.sleep(3)

    # Check that the page header is as expected
    page_header = 'Шезлонги та лежаки'

    assert epic_page.check_page_header(page_header)

    time.sleep(3)

    # Close browser
    epic_page.close()


@pytest.mark.ui_epic
def test_check_product_can_be_ordered_page_object():
    # Create page object
    epic_page = Epicentr()

    # Open page https://epicentrk.ua/
    epic_page.go_to()

    time.sleep(3)

    # Try to search product
    search_product = 'Шезлонг'
    epic_page.try_search_product(search_product)

    time.sleep(3)

    # Check order
    title = 'ОФОРМЛЕННЯ ЗАМОВЛЕННЯ'
    
    assert epic_page.check_order_product(title)

    time.sleep(3)

    # Close browser
    epic_page.close()