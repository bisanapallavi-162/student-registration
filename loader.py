import csv
from validator import validate_record

INPUT_FILE = "contacts.csv"
OUTPUT_FILE = "students_clean.csv"

def clean_contacts():
    seen_phones = set()
    seen_emails = set()
    clean_rows = []
    rejected_rows = []

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=2):
            errors = validate_record(row)
            phone = row.get("phone", "").strip()
            email = row.get("email", "").strip().lower()

            if phone in seen_phones:
                errors.append("Duplicate phone")
            if email in seen_emails:
                errors.append("Duplicate email")

            if errors:
                rejected_rows.append((row_number, row, errors))
            else:
                seen_phones.add(phone)
                seen_emails.add(email)
                clean_rows.append({
                    "name": row["name"].strip(),
                    "phone": phone,
                    "email": email
                })

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone", "email"])
        writer.writeheader()
        writer.writerows(clean_rows)

    print(f"Cleaning completed. {len(clean_rows)} clean record(s) saved to {OUTPUT_FILE}.")
    print(f"{len(rejected_rows)} record(s) rejected.")
    for row_number, row, errors in rejected_rows:
        print(f"Row {row_number}: {', '.join(errors)}")

    return clean_rows, rejected_rows

if __name__ == "__main__":
    clean_contacts()
