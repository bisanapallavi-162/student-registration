import csv
from collections import Counter

def show_report(filename="students_clean.csv"):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
    except FileNotFoundError:
        print("Clean data file not found. Please run the cleaning option first.")
        return

    print("\\n--- CONTACT BUSINESS REPORT ---")
    print(f"Total clean contacts : {len(rows)}")
    domains = Counter(row["email"].split("@")[-1].lower() for row in rows)
    print("Email domain summary:")
    for domain, count in domains.most_common():
        print(f"  {domain}: {count}")
