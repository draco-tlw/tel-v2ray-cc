from datetime import datetime


def parse_iso_date(date_str: str):
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        print(f"[!] Error: Invalid ISO format in string: '{date_str}'")
