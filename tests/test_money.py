import pytest
from money import Money
from currency import Currency


CURRENCY3 = Currency('Euro', 'EUR', 978, u'\u20AC', False, 3)


# Init

def test_init():
    assert Money(12) == Money(12.00) == Money("12")


def test_grains():
    m = Money(12)
    assert m.grains == 1200
    m.set_currency(CURRENCY3)
    assert m.grains == 12000


# Comparison Operators

def test_le():
    assert Money(12.00) <= Money(13.000)
    with pytest.raises(TypeError):
        assert Money(13.00) <= Money(13.000, CURRENCY3)


def test_lt():
    assert Money(12.00) < Money(13.000)
    with pytest.raises(TypeError):
        assert Money(12.00) < Money(13.000, CURRENCY3)


def test_eq():
    assert Money(13.00) == Money(13.000)
    with pytest.raises(TypeError):
        assert Money(13.00) == Money(13.000, CURRENCY3)


def test_ne():
    assert not Money(14.00) == Money(13.000)
    with pytest.raises(TypeError):
        assert not Money(14.00) == Money(13.000, CURRENCY3)


def test_ge():
    assert Money(14.00) >= Money(13.000)
    with pytest.raises(TypeError):
        assert Money(14.00) >= Money(13.000, CURRENCY3)
    assert Money(13.00) >= Money(13.000)
    with pytest.raises(TypeError):
        assert Money(13.00) >= Money(13.000, CURRENCY3)


def test_gt():
    assert Money(14.00) > Money(13.000)
    with pytest.raises(TypeError):
        assert Money(14.00) > Money(13.000, CURRENCY3)


# Arithmetic Operators

def test_abs():
    assert abs(Money(14)) == abs(Money(-14)) == Money(14)


def test_add():
    assert Money(10) + Money(20) == Money(30)
    with pytest.raises(TypeError):
        assert Money(10) + Money(20, CURRENCY3) == Money(30, CURRENCY3)


def test_div():
    assert Money(30) / 3 == Money(10)


def test_iadd():
    m = Money(10)
    m += Money(20)
    assert m == Money(30)
    assert m.grains == 3000


def test_idiv():
    m = Money(30)
    m /= 3
    assert m == Money(10)


def test_imul():
    m = Money(10)
    m *= 3
    assert m == Money(30)


def test_isub():
    m = Money(30)
    m -= Money(20)
    assert m == Money(10)
    assert m.grains == 1000


def test_mul():
    assert Money(10) * 3 == Money(30)


def test_neg():
    assert -Money(-30) == Money(30)


def test_sub():
    assert Money(30) - Money(20) == Money(10)
    assert Money(10) - Money(20) == -Money(10)
    with pytest.raises(TypeError):
        assert Money(30) - Money(20, CURRENCY3) == Money(10, 3)
