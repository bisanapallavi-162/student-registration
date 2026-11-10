import re

def validate_name(name):
    return bool(name and name.strip())

def validate_phone(phone):
    phone = str(phone).strip()
    return phone.isdigit() and len(phone) == 10 and phone[0] in "6789"

def validate_email(email):
    email = str(email).strip()
    return (
        email.count("@") == 1
        and " " not in email
        and "." in email.split("@")[1]
        and bool(email.split("@")[0])
        and bool(email.split("@")[1])
    )

def validate_record(record):
    errors = []
    name = record.get("name", "")
    phone = record.get("phone", "")
    email = record.get("email", "")

    if not validate_name(name):
        errors.append("Name is blank")
    if not validate_phone(phone):
        errors.append("Phone must be 10 digits and start with 6, 7, 8 or 9")
    if not validate_email(email):
        errors.append("Email format is invalid")

    return errors
