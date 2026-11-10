# Student Registration & Contact Intelligence System

**Student Name:** Bisana Pallavi  
**Course:** BCA Semester 1 - Basics of Python  
**Batch:** Batch 1  
**College:** Christ Academy

## Project Overview
A Python-based system to clean and manage coaching-centre contacts. It reads
`contacts.csv`, validates records, rejects invalid and duplicate records, and
saves valid records in `students_clean.csv`.

## Validation Rules
- Name must not be blank.
- Phone must contain exactly 10 digits, contain digits only, and start with 6, 7, 8 or 9.
- Email must contain exactly one `@`, no spaces, and a dot in the domain.
- A repeated phone number or email address is rejected.

## Project Files
1. `main.py` - Menu-driven system.
2. `validator.py` - Validation functions.
3. `loader.py` - Reads, validates and cleans CSV records.
4. `analytics.py` - Displays a summary report.
5. `contacts.csv` - Sample input data (20 records).
6. `students_clean.csv` - Generated clean output.
7. `README.md` - Project documentation.

## How to Run
Open a terminal in this project folder and run:

```bash
python loader.py
python main.py
```

You can also run `main.py` first and choose option 1 to clean the data.
The program uses only Python's built-in modules; no installation is required.
