from datetime import date

from src.date_utils import is_valid_iso_date


def test_valid_standard_date():
    assert is_valid_iso_date("2026-05-27") is True


def test_valid_january_first():
    assert is_valid_iso_date("2026-01-01") is True


def test_valid_december_last():
    assert is_valid_iso_date("2026-12-31") is True


def test_valid_leap_day():
    assert is_valid_iso_date("2024-02-29") is True


def test_invalid_month_thirteen():
    assert is_valid_iso_date("2026-13-01") is False


def test_invalid_day_for_month():
    assert is_valid_iso_date("2026-02-30") is False


def test_invalid_non_leap_feb_29():
    assert is_valid_iso_date("2023-02-29") is False


def test_invalid_month_zero():
    assert is_valid_iso_date("2026-00-15") is False


def test_invalid_day_zero():
    assert is_valid_iso_date("2026-05-00") is False


def test_invalid_empty_string():
    assert is_valid_iso_date("") is False


def test_invalid_none():
    assert is_valid_iso_date(None) is False


def test_invalid_slash_separator():
    assert is_valid_iso_date("2026/05/27") is False


def test_invalid_dot_separator():
    assert is_valid_iso_date("2026.05.27") is False


def test_invalid_missing_zero_pad_month():
    assert is_valid_iso_date("2026-5-27") is False


def test_invalid_missing_zero_pad_day():
    assert is_valid_iso_date("2026-05-7") is False


def test_invalid_reversed_order():
    assert is_valid_iso_date("27-05-2026") is False


def test_invalid_leading_whitespace():
    assert is_valid_iso_date(" 2026-05-27") is False


def test_invalid_trailing_whitespace():
    assert is_valid_iso_date("2026-05-27 ") is False


def test_invalid_with_time_suffix():
    assert is_valid_iso_date("2026-05-27T00:00:00") is False


def test_invalid_compact_form():
    assert is_valid_iso_date("20260527") is False


def test_invalid_non_string_int():
    assert is_valid_iso_date(20260527) is False


def test_invalid_non_string_date_object():
    assert is_valid_iso_date(date(2026, 5, 27)) is False


def test_invalid_garbage_string():
    assert is_valid_iso_date("hello") is False
