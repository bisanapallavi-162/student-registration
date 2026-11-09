"""Validation functions for student contact records."""
import re

def validate_record(record):
    """Return (is_valid, reason). Name, 10-digit phone, and email are required."""
    name = record.get("name", "").strip()
    phone = record.get("phone", "").strip()
    email = record.get("email", "").strip()

    if not name:
        return False, "Missing name"
    if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", name):
        return False, "Name contains invalid characters"
    if not re.fullmatch(r"[6-9]\d{9}", phone):
        return False, "Phone must be a valid 10-digit Indian mobile number"
    if not re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
        return False, "Invalid email format"
    return True, "Valid"
