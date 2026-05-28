from datetime import datetime


def is_valid_iso_date(s: str) -> bool:
    if not isinstance(s, str):
        return False
    if len(s) != 10:
        return False
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False
