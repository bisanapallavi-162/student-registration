"""Business intelligence summaries for validated student contacts."""
from collections import Counter

def show_analytics(total, valid_records, rejected_records):
    valid_count = len(valid_records)
    rejected_count = len(rejected_records)
    accuracy = (valid_count / total * 100) if total else 0

    print("\n" + "=" * 55)
    print("       STUDENT REGISTRATION - BUSINESS INTELLIGENCE")
    print("=" * 55)
    print(f"Total Contacts Processed : {total}")
    print(f"Valid Registrations      : {valid_count}")
    print(f"Rejected Records         : {rejected_count}")
    print(f"Data Quality Accuracy    : {accuracy:.1f}%")

    networks = Counter()
    domains = Counter()
    for record in valid_records:
        phone = record["phone"]
        networks[phone[0] + "-Series"] += 1
        domain = "@" + record["email"].split("@")[-1].lower()
        domains[domain] += 1

    print("\n--- Telecom Prefix Breakdown ---")
    for prefix in sorted(networks):
        print(f"{prefix:12}: {networks[prefix]} students")

    print("\n--- Top Email Domains ---")
    for domain, count in domains.most_common():
        print(f"{domain:25}: {count} students")
    print("=" * 55)
