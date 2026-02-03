from datetime import datetime

def normalize_text(value: str, field_name: str) -> str:
    text = (value or "").strip()
    if not text:
        raise ValueError(f"{field_name} cannot be empty.")
    return text

def parse_date(date_str: str):
    try:
        return datetime.strptime((date_str or "").strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def parse_amount(amount_str: str) -> float:
    try:
        return float((amount_str or "").strip())
    except ValueError:
        raise ValueError("Amount must be a number.")

def parse_index(index_str: str) -> int:
    try:
        return int((index_str or "").strip())
    except ValueError:
        raise ValueError("Index must be a number.")