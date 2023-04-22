"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv

item = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    assert item.apply_discount() == None


# def test_instantiate_from_csv():
#     assert item.instantiate_from_csv() ==('Клавиатура', 75, 5)

def test_name():
    assert item.name == 'Смартфон'
    if item.name == 'СуперСмартфон':
        assert "Exception: Длина наименования товара превышает 10 символов"

def test_string_to_number():
    assert Item.string_to_number('6.0') == 6





