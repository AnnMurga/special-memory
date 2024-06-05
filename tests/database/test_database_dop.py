import pytest
from modules.common.database import Database
from sqlite3 import OperationalError

@pytest.mark.database_dop
def test_product_not_insert_with_incorrect_id_type():
    with pytest.raises(OperationalError):
        db = Database()
        db.insert_product('qwe', 'шоколад', 'гіркий', 70)

@pytest.mark.database_dop
def test_product_insert_with_quantity_string():
    db = Database()
    db.insert_product(5, 'шоколад', 'гіркий', '70')
    new_product = db.select_product_qnt_by_id(5)

    assert new_product[0][0] == 70

@pytest.mark.database_dop
def test_product_insert_with_name_integer():
    db = Database()
    db.insert_product(6, 908765, 'з арахісом', 15)
    new_product = db.select_product_qnt_by_id(6)

    assert new_product[0][0] == 15

@pytest.mark.database_dop
def test_customer_insert():
    db = Database()
    db.insert_customer(3, 'Taras', 'Shevchenko ave, 61', 'Kharkiv', '6100', 'Ukraine')
    new_customer = db.select_customer_name_by_id(3)
    
    assert new_customer[0][0] == 'Taras'

@pytest.mark.database_dop
def test_customer_insert_with_name_integer():
    db = Database()
    db.insert_customer(4, 5477, 'Nezalezhnosti sq, 3', 'Kharkiv', '6120', 'Ukraine')
    new_customer = db.select_customer_name_by_id(4)
    
    assert new_customer[0][0] == '5477'

@pytest.mark.database_dop
def test_customer_insert_with_city_integer():
    db = Database()
    db.insert_customer(5, 'Vasyl', 'Perevoga, 5', 890, '6148', 'Ukraine')
    new_customer = db.select_customer_name_by_id(5)
    
    assert new_customer[0][0] == 'Vasyl'

@pytest.mark.database_dop
def test_customer_not_insert_with_incorrect_id_type():
    with pytest.raises(OperationalError):
        db = Database()
        db.insert_customer('zxc', 4567, 'Uvileiniy ave', 'Kharkiv', '6107', 'Ukraine')

@pytest.mark.database_dop
def test_order_insert_with_date_string():
    db = Database()
    db.insert_order(2, 3, 2, "2024-05-12")
    new_order = db.select_detailed_order_by_id(2)

    assert new_order[0][0] == 2

@pytest.mark.database_dop
def test_order_insert_with_date_integer():
    db = Database()
    db.insert_order(3, 2, 2, 123452)
    new_order = db.select_detailed_order_by_id(3)

    assert new_order[0][1] == 'Stepan'

@pytest.mark.database_dop
def test_order_not_insert_with_incorrect_date_type():
    with pytest.raises(OperationalError):
        db = Database()
        db.insert_order(2, 3, 2, '10:15:05')
