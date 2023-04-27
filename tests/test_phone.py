from src.item import Item
from src.phone import Phone
import pytest

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number():
    with pytest.raises(TypeError):
        phone1.number_of_sim = 0



def test_number_property():
    assert phone1.number_of_sim == 2

