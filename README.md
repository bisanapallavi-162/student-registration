# Student Registration & Contact Intelligence System

**Course:** BCA Semester 1 — Python Programming  
**Student:** B.pallavi 
**Section:** C

## Project overview
This beginner-friendly Python project reads student contacts from `contacts.csv`, checks names, Indian mobile numbers and email addresses, rejects invalid or duplicate entries, lets a user view/search/add students, and prints a simple business-intelligence report.

## Files
- `main.py` — menu and main program
- `validator.py` — validates name, phone and email
- `loader.py` — reads CSV, rejects bad/duplicate records, saves clean records
- `analytics.py` — prints data-quality, phone-prefix and email-domain summaries
- `contacts.csv` — sample input records
- `clean_contacts.csv` — generated automatically when the program runs
- `proof/` — place your own screenshots of the program running here

## How to run
1. Install Python 3 if it is not already installed.
2. Keep all `.py` files and `contacts.csv` in the same folder.
3. Open a terminal/command prompt in this folder.
4. Run: `python main.py`
5. Select menu options 1 to 6.

On some computers, use `python3 main.py` instead.

## What to test
- View all valid students (option 1)
- Search for a student by name or phone (option 2)
- Add a valid student and then check `clean_contacts.csv` (option 3)
- Print the business-intelligence report (option 4)
- View rejected rows and their reasons (option 5)
- Exit (option 6)

## Concepts used
Variables, strings, lists, dictionaries, functions, loops, conditional statements, regular expressions, CSV file handling, and `Counter` for simple summaries.

## Student self-notes — edit this in your own words
I learned how to read CSV data, validate user input, use lists and dictionaries to store records, prevent duplicate entries, and create summary reports. One challenge was checking invalid and repeated phone numbers or email addresses.
