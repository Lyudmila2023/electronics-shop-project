"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import csv

item = Item("Смартфон", 10000, 20)


def test_init():
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_repr():
    assert str(item) == 'Смартфон'


def test_calculate_total_price():
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    assert item.apply_discount() is None


def test_instantiate_from_csv():
    assert len(item.instantiate_from_csv()) == 3


def test_name():
    assert item.name == 'Смартфон'
    if item.name == 'СуперСмартфон':
        assert "Exception: Длина наименования товара превышает 10 символов"


def test_string_to_number():
    assert Item.string_to_number('6.0') == 6





