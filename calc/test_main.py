import calc
import pytest


def test_add():
    assert calc.add(2, 3) == 5
    assert calc.add(2, 3, 4) == 9
    assert calc.add(2) == 2


def test_sub():
    assert calc.sub(5, 3) == 2
    assert calc.sub(0, 0) == 0
    assert calc.sub(10, 20) == -10
