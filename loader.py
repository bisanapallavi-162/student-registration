"""Load, validate, and save student contact records from CSV files."""
import csv
from validator import validate_record

def load_contacts(filename="contacts.csv"):
    valid_records = []
    rejected_records = []
    seen_phones = set()
    seen_emails = set()

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            record = {
                "name": row.get("name", "").strip(),
                "phone": row.get("phone", "").strip(),
                "email": row.get("email", "").strip()
            }
            ok, reason = validate_record(record)
            if not ok:
                rejected_records.append((record, reason))
                continue

            phone_key = record["phone"]
            email_key = record["email"].lower()
            if phone_key in seen_phones or email_key in seen_emails:
                rejected_records.append((record, "Duplicate phone or email"))
                continue

            seen_phones.add(phone_key)
            seen_emails.add(email_key)
            valid_records.append(record)

    return valid_records, rejected_records

def save_contacts(records, filename="clean_contacts.csv"):
    """Save clean records to a new CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(records)
