import json
import pytest

def test_load_orders_list():
    try:
        with open("data/orders_list.json", 'r') as file:
            orders_list = json.load(file)
        assert orders_list is not None
    except FileNotFoundError:
        pytest.fail("orders_list.json not found")

def test_load_products_list():
    try:
        with open("data/products_list.json", 'r') as file:
            products_list = json.load(file)
        assert products_list is not None
    except FileNotFoundError:
        pytest.fail("products_list.json not found")

def test_load_couriers_list():
    try:
        with open("data/couriers_list.json", 'r') as file:
            courier_list = json.load(file)
        assert courier_list is not None
    except FileNotFoundError:
        pytest.fail("couriers_list.json not found")