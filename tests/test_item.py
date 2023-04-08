"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
item = Item("Смартфон", 10000, 20)
# def test_init():
#     assert Item("Смартфон", 10000, 20) == '<src.item.Item object at 0x00000221107603D0>'
def test_calculate_total_price():

    assert item.calculate_total_price() == 200000


def test_apply_discount():
    assert item.apply_discount() == None


