import pytest

from src.discount import calculate_discount

def test_ep_small_purchase_non_member():
    assert calculate_discount(20.00, is_member=False) == 20.00;

def test_ep_large_purchase_member():
    assert calculate_discount(100.00, is_member=True) == 85.50;

def test_ep_invalid_purchase_raises():
    with pytest.raises(ValueError):
        calculate_discount(-10.00, is_member=False);

def test_bva_just_below_threshold():
    assert calculate_discount(49.99, is_member=False) == 49.99;

def test_bva_exactly_at_threshold():
    assert calculate_discount(50.00, is_member=False) == 45.00;

def test_bva_zero_purchase():
    assert calculate_discount(0.00, is_member=False) == 0.00;