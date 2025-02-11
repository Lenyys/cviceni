import pytest
from p10_priklad_5 import Product, Warehouse


@pytest.fixture
def products():
    return [Product("box_shoes", 10.3), Product("box_apples", 20.4),
            Product("box_oranges", 15.2), Product("box_water_bottles", 40.5)]


@pytest.mark.parametrize("kapacity, result", [(10, -1), (86.4, 0), (100, 13.6)])
def test_warehouse(products, kapacity, result):
    warehouse = Warehouse(kapacity)
    returned_value = 0
    for product in products:
        returned_value = warehouse.add(product)
    assert round(returned_value, 1) == result

