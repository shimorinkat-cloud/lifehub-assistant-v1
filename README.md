# LifeHub Assistant v1

LifeHub Assistant is a command-line personal assistant built with Python.

The application helps users manage contacts and notes directly from the terminal.
It supports data validation, search, editing, deletion, tags for notes, and data persistence using pickle.

---

# Features

## Contacts

- Add contacts
- Edit contacts
- Show all contacts
- Search contacts
- Delete contacts
- Find upcoming birthdays
- Validate phone numbers
- Validate email addresses
- Validate birthday format

## Notes

- Add notes
- Edit notes
- Show all notes
- Search notes
- Delete notes
- Add tags to notes
- Search notes by tags

## Data Storage

- Save data to a local file
- Load data after application restart
- Store contacts and notes using pickle

---

# Project Structure

```text
lifehub-assistant-v1/
├── main.py
├── contacts.py
├── notes.py
├── storage.py
├── validators.py
├── commands.py
├── README.md
├── requirements.txt
├── .gitignore
└── data/
    └── assistant_data.pkl
```

---

# Requirements

- Python 3.10 or higher

---

# Installation

Clone the repository:

```bash
git clone https://github.com/shimorinkat-cloud/lifehub-assistant-v1.git
```

Go to the project folder:

```bash
cd lifehub-assistant-v1
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment on Windows:

```bash
venv\Scripts\activate
```

Run the application:

```bash
python main.py
```

---

# Available Commands

## Contacts

```text
add-contact
show-contacts
search-contact
edit-contact
delete-contact
birthdays
```

## Notes

```text
add-note
show-notes
search-note
edit-note
delete-note
```

## System

```text
save
help
exit
```

---

# Usage Example

```text
Enter command: add-contact

Name: Roman
Phone: +380671234567
Email: roman@test.com
Address: Katowice
Birthday: 17.11.1991

Contact added successfully.
```

```text
Enter command: show-contacts

Name: Roman, Phone: +380671234567,
Email: roman@test.com,
Address: Katowice,
Birthday: 17.11.1991
```

---

# Data Persistence

The application saves data to:

```text
data/assistant_data.pkl
```

When the application is restarted, saved contacts and notes are loaded automatically.

---

# Code Quality

The project uses:

- Object-Oriented Programming
- Type hints
- Docstrings
- Modular structure
- Basic error handling
- PEP 8 style recommendations

---

# Authors

Team project for Python Programming discipline.

---

# Version

1.0.0
