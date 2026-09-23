# Library Management System

A menu-driven Python console application developed for the **CSC-1024 assignment at Sunway University**. The project organizes a book collection using object-oriented classes, terminal menus, and a local text file.

It includes code for adding, editing, deleting, listing, and searching books, with reading statuses of `read`, `to-read`, and `reading`.

> **Project status:** coursework prototype with known issues. A fresh checkout has an import-path problem that prevents normal startup, and the save routine needs correction before it can reliably preserve records. See [Known issues](#known-issues) before running it with data you want to keep.

## Features and workflow

The application is organized around four main menu options:

| Option | Purpose |
| --- | --- |
| **1 — Add/Edit Books** | Enter a new book or locate a book by ISBN and update its details. |
| **2 — Delete Books** | Remove a matching book from the collection. |
| **3 — Display Books** | List all records or search for a matching value. |
| **4 — Exit** | Leave the menu loop and write records back to `book_list.txt`. |

Search compares the entered text against all eight fields using **exact, case-sensitive matching**. It does not perform partial-title or keyword searches.

Changes are held in memory during a session. The program attempts to save them only when the main menu's Exit option is selected.

## Getting started

### Requirements

- Python 3. The source uses f-strings, which require Python 3.6 or later; the repository does not declare a tested Python version.
- A terminal.
- Git, or a downloaded ZIP of the repository.

The application uses the Python standard library and local modules. No third-party package installation is specified.

### Download the project

```sh
git clone https://github.com/beksus/CSC-1024-Assignment.git
cd CSC-1024-Assignment
```

### Resolve the startup import

`AddEdit.py` imports `Validator` as a top-level module, but its source is located at `test/Validator.py`. On a normal fresh checkout, running the application raises:

```text
ModuleNotFoundError: No module named 'Validator'
```

The imported class is not used by the current `AddEdit.py` implementation. To try the application, remove the unused `from Validator import Validator` line, or correct it to `from test.Validator import Validator`.

This only resolves startup; the save and input-handling issues below still need attention.

### Launch

Run from the repository root so that the relative path to `book_list.txt` resolves correctly:

```sh
python LibraryMain.py
```

Use `python3` instead of `python` if that is the Python 3 command on your system.

Keep a backup of `book_list.txt` before experimenting: exiting rewrites the file, and the current writer produces an incorrect field layout.

## Book data

Each record contains eight fields in this order:

```text
ISBN,author,title,publisher,genre,year_published,date_purchased,status
```

For example:

```text
9780747532686,JK Rowling,Harry Potter and the Philosopher's Stone,Bloomsbury,Fantasy,1997,15-03-2020,to-read
```

The repository includes 20 sample records. Publication years are stored as text, purchase dates use the `DD-MM-YYYY` format, and reading status is one of `read`, `to-read`, or `reading`.

The loader splits each line directly on commas rather than using a CSV parser. Fields must not contain commas, and records need all eight fields. There is no database or external service.

## Project structure

| File | Responsibility |
| --- | --- |
| [LibraryMain.py](LibraryMain.py) | Entry point, file loading, main menu, and save-on-exit logic. |
| [Book.py](Book.py) | Book model with indexed getters and update methods. |
| [AddEdit.py](AddEdit.py) | Interactive prompts for adding and editing records. |
| [Delete.py](Delete.py) | Matching and removal of a book from the in-memory collection. |
| [Display.py](Display.py) | ASCII artwork, menus, record display, search, and terminal clearing. |
| [book_list.txt](book_list.txt) | Comma-separated sample book collection. |
| [test/Validator.py](test/Validator.py) | Experimental input-validation helper. |
| [test/test.py](test/test.py) | Manual development script for loading, displaying, and editing records. |

The `test/` directory contains development scripts rather than an automated test suite. The repository also includes IDE settings and Python bytecode caches.

## Known issues

The following limitations are visible in the current source:

- **Startup import:** `Validator.py` is not located where the top-level import expects it.
- **Incorrect save format:** `LibraryMain.py` writes the publication-year field twice, producing nine fields instead of eight. Reloading shifts the purchase date and status into the wrong positions. The final `file.close` reference also lacks parentheses.
- **Incomplete validation:** several checks reference methods such as `isdigit`, `isalpha`, and `isalnum` without calling them, so invalid input can pass.
- **Edit-menu mismatch:** the Title and Author menu labels are reversed relative to the prompts and stored fields. Repeated unsuccessful ISBN lookups can also leave the selected book index incorrect.
- **Delete-menu mismatch:** the prompt suggests ISBN or title, but the implementation matches ISBN, author, or reading status and removes the first match. Title matching is not implemented.
- **Limited file handling:** missing files, malformed rows, and comma-containing values are not handled robustly. Some sample field values also need review.

Useful next steps are to fix record serialization, align menus with the book model, complete input validation, and add tests for editing, deletion, and saving/reloading records.

## License

No license file is currently included in the repository.

